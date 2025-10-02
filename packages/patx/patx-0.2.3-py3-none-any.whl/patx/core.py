"""
Core PatternOptimizer class for extracting polynomial patterns from time series data.
"""

import json
import os
from typing import Optional, Union, List, Dict, Tuple, Callable, Any
import numpy as np
from numpy.typing import NDArray
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import optuna
from sklearn.model_selection import train_test_split

from .models import evaluate_model_performance, clone_model, get_model

optuna.logging.set_verbosity(optuna.logging.WARNING)

class PatternExtractor:
    """
    Extract polynomial patterns from time series data for feature engineering.
    
    This class uses Optuna optimization to find polynomial patterns in time series
    that are most predictive for the target variable.
    """
    
    def __init__(
        self, 
        X_train: Union[NDArray[np.float32], List[NDArray[np.float32]]], 
        y_train: NDArray[np.float32], 
        X_test: Optional[Union[NDArray[np.float32], List[NDArray[np.float32]]]] = None,
        dataset: Optional[str] = None, 
        model: Optional[Any] = None,
        max_n_trials: Optional[int] = None, 
        n_jobs: Optional[int] = None, 
        show_progress: Optional[bool] = None,
        metric: Optional[str] = None, 
        polynomial_degree: Optional[int] = None,
        val_size: Optional[float] = None, 
        initial_features: Optional[Union[NDArray[np.float32], Tuple[NDArray[np.float32], NDArray[np.float32]]]] = None, 
        pattern_fn: Optional[Callable[[List[float], int], NDArray[np.float32]]] = None, 
        similarity_fn: Optional[Callable[[NDArray[np.float32], NDArray[np.float32]], NDArray[np.float32]]] = None
    ) -> None:
        """
        Initialize PatternExtractor.
        
        Parameters
        ----------
        X_train : array-like or list of arrays
            Training data. If list, automatically handles multiple time series.
        y_train : array-like
            Training targets
        X_test : array-like or list of arrays, optional
            Test data for feature extraction (same structure as X_train)
        dataset : str, optional
            Dataset name (default: 'default')
        model : object, optional
            Model with fit() and predict() methods. Defaults to LightGBM.
        max_n_trials : int, optional
            Maximum number of optimization trials (default: 50)
        n_jobs : int, optional
            Number of parallel jobs for optimization (default: -1)
        show_progress : bool, optional
            Whether to show progress bar (default: True)
        metric : str, optional
            Evaluation metric ('rmse', 'accuracy', 'auc'). If None, inferred (default: None)
        polynomial_degree : int, optional
            Degree of polynomial patterns (default: 3)
        val_size : float, optional
            Validation size (default: 0.3)
        initial_features : array-like, optional
            Initial features to include
        pattern_fn : callable, optional
            Custom pattern creation function(coeffs, n_points). Defaults to polynomial_pattern.
        similarity_fn : callable, optional
            Custom similarity calculation function(X_region, pattern_values). Defaults to calculate_pattern_rmse.
        """
        # Auto-detect multiple series from X_train structure
        self.multiple_series = isinstance(X_train, list)

        # Normalize X_train into expected internal shape
        if self.multiple_series and isinstance(X_train, list):
            self.X_series_list = [np.asarray(x, dtype=np.float32) for x in X_train]
            self.X_train = np.stack(self.X_series_list, axis=1)
        else:
            self.X_series_list = None
            self.X_train = np.asarray(X_train, dtype=np.float32)

        self.y_train = np.asarray(y_train, dtype=np.float32)

        # Store X_test with new name
        self.X_test = X_test

        # Set defaults for optional parameters
        self.max_n_trials = max_n_trials if max_n_trials is not None else 50
        self.n_jobs = n_jobs if n_jobs is not None else -1
        self.show_progress = show_progress if show_progress is not None else True
        self.dataset = dataset if dataset is not None else 'df'
        self.polynomial_degree = polynomial_degree if polynomial_degree is not None else 3
        self.val_size = val_size if val_size is not None else 0.3

        # Defaults for control params
        self.pattern_list = []
        self.pattern_starts = []
        self.pattern_ends = []
        self.pattern_series_indices = []
        # Determine task type and defaults
        unique_targets = np.unique(self.y_train)
        is_classification = unique_targets.size <= 20 and np.allclose(unique_targets, unique_targets.astype(int))
        if model is None:
            task_type = 'classification' if is_classification else 'regression'
            n_classes = int(unique_targets.size) if task_type == 'classification' else None
            self.model = get_model(task_type, dataset, n_classes=n_classes)
        else:
            self.model = model
        if metric is None:
            if is_classification:
                # Prefer AUC for binary problems, else accuracy
                self.metric = 'auc' if unique_targets.size == 2 else 'accuracy'
            else:
                self.metric = 'rmse'
        else:
            self.metric = metric
        self.features_list = []
        self.best_score = float('inf') if self.metric == 'rmse' else -float('inf')
        self.initial_features = initial_features
        self.pattern_fn = pattern_fn if pattern_fn is not None else self.polynomial_pattern
        self.similarity_fn = similarity_fn if similarity_fn is not None else self.calculate_pattern_rmse
    
    def __str__(self) -> str:
        """String representation of PatternExtractor."""
        n_patterns = len(self.pattern_list)
        series_info = f" ({len(self.X_series_list)} series)" if self.multiple_series else ""
        return f"PatternExtractor(dataset='{self.dataset}', patterns={n_patterns}{series_info}, metric='{self.metric}')"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"PatternExtractor(X_train={self.X_train.shape}, y_train={self.y_train.shape}, "
                f"dataset='{self.dataset}', patterns={len(self.pattern_list)}, metric='{self.metric}')")
    
    def __len__(self) -> int:
        """Return number of extracted patterns."""
        return len(self.pattern_list)
    
    def __getitem__(self, idx: int) -> Dict[str, Any]:
        """Get pattern by index."""
        if idx < 0 or idx >= len(self.pattern_list):
            raise IndexError(f"Pattern index {idx} out of range [0, {len(self.pattern_list)})")
        
        pattern_info = {
            'pattern': self.pattern_list[idx],
            'start': self.pattern_starts[idx],
            'end': self.pattern_ends[idx],
        }
        if self.multiple_series and self.pattern_series_indices:
            pattern_info['series_index'] = self.pattern_series_indices[idx]
        return pattern_info
    
    def __iter__(self):
        """Iterate over patterns."""
        for i in range(len(self.pattern_list)):
            yield self[i]
    
    @property
    def n_patterns(self) -> int:
        """Number of extracted patterns."""
        return len(self.pattern_list)
    
    @property
    def patterns(self) -> List[NDArray[np.float32]]:
        """List of all extracted patterns."""
        return self.pattern_list
    
    def polynomial_pattern(self, coeffs: List[float], n_points: int) -> NDArray[np.float32]:
        """Generate polynomial pattern from coefficients."""
        x = np.linspace(-1, 1, n_points, dtype=np.float32)
        coeffs = np.array(coeffs, dtype=np.float32)
        powers = np.arange(len(coeffs), dtype=np.float32)
        return np.sum(coeffs * (x[:, None] ** powers), axis=1)

    def calculate_pattern_rmse(self, X_region: NDArray[np.float32], pattern_values: NDArray[np.float32]) -> NDArray[np.float32]:
        """Calculate RMSE between data region and pattern."""
        return np.sqrt(np.mean((X_region - pattern_values) ** 2, axis=1))

    def objective(self, trial: optuna.Trial, dim: int) -> float:
        """Optuna objective function for pattern optimization."""
        series_index = trial.suggest_int('series_index', 0, self.X_train.shape[1] - 1) if self.multiple_series else None
        pattern_start = trial.suggest_int('pattern_start', 0, dim - 2)
        pattern_width = trial.suggest_int('pattern_width', 1, dim - pattern_start)
        coeffs = [trial.suggest_float(f'c{i}', -1, 1) for i in range(self.polynomial_degree + 1)]
        X_data = self.X_train[:, series_index, :] if self.multiple_series and series_index is not None and self.X_train.ndim == 3 else self.X_train
        X_region = X_data[:, pattern_start:pattern_start + pattern_width]
        new_feature = self.similarity_fn(X_region, self.pattern_fn(coeffs, pattern_width))
        X_combined = np.column_stack(self.features_list + [new_feature]) if self.features_list else new_feature.reshape(-1, 1)
        X_train, X_val, y_train, y_val = train_test_split(X_combined, self.y_train, test_size=self.val_size, random_state=42)
        model = clone_model(self.model)
        
        model.fit(X_train, y_train, X_val, y_val)
        return evaluate_model_performance(model, X_val, y_val, self.metric)
    
    def feature_extraction(self, X_series_list: Optional[List[NDArray[np.float32]]] = None) -> Dict[str, Any]:
        """
        Extract features using optimized polynomial patterns.
        
        Parameters
        ----------
        X_series_list : list, optional
            List of time series data
            
        Returns
        -------
        dict
            Dictionary containing patterns, features, and model results
        """
        first_pattern = True
        if X_series_list is not None and self.multiple_series:
            self.X_series_list = [np.asarray(x, dtype=np.float32) for x in X_series_list]
            self.X_train = np.stack(self.X_series_list, axis=1)
        dim = self.X_train.shape[2] if self.multiple_series and self.X_train.ndim == 3 else self.X_train.shape[1]
        train_initial_features, test_initial_features = (None, None) if self.initial_features is None else ((np.asarray(self.initial_features[0], dtype=np.float32), np.asarray(self.initial_features[1], dtype=np.float32)) if isinstance(self.initial_features, tuple) and len(self.initial_features) == 2 else (np.asarray(self.initial_features, dtype=np.float32), None))
        if train_initial_features is not None: 
            self.features_list = [train_initial_features]
        
        while True:
            study = optuna.create_study(direction="minimize" if self.metric == 'rmse' else "maximize", pruner=optuna.pruners.MedianPruner())
            study.optimize(lambda trial: self.objective(trial, dim), n_trials=self.max_n_trials, n_jobs=self.n_jobs, show_progress_bar=self.show_progress)
            if first_pattern or (self.metric == 'rmse' and study.best_value < self.best_score) or (self.metric != 'rmse' and study.best_value > self.best_score):
                self.best_score = study.best_value
                best_params = study.best_trial.params
                pattern_start = best_params['pattern_start']
                pattern_width = best_params['pattern_width']
                coeffs = [best_params[f'c{i}'] for i in range(self.polynomial_degree + 1)]
                series_index = best_params.get('series_index')
                pattern_values = self.pattern_fn(coeffs, pattern_width)
                pattern_end = pattern_start + pattern_width
                new_pattern = np.zeros(dim, dtype=np.float32)
                new_pattern[pattern_start:pattern_end] = pattern_values
                self.pattern_list.append(new_pattern)
                self.pattern_starts.append(pattern_start)
                self.pattern_ends.append(pattern_end)
                if self.multiple_series:
                    self.pattern_series_indices.append(series_index)
                X_data = self.X_train
                if self.multiple_series and series_index is not None and X_data.ndim == 3:
                    X_data = X_data[:, series_index, :]
                X_region = X_data[:, pattern_start:pattern_end]
                new_feature_full = self.similarity_fn(X_region, pattern_values)
                self.features_list.append(new_feature_full)
                first_pattern = False
            else:
                break
        
        cached_features = np.column_stack(self.features_list) if self.features_list else np.empty((self.X_train.shape[0], 0))
        X_train, X_val, y_train, y_val = train_test_split(cached_features, self.y_train, test_size=self.val_size, random_state=42)
        self.model.fit(X_train, y_train, X_val, y_val)
        n_test_samples = self.X_test[0].shape[0] if isinstance(self.X_test, list) else self.X_test.shape[0]
        n_pattern_features = len(self.pattern_list)
        n_initial_features = train_initial_features.shape[1] if train_initial_features is not None else 0
        X_test = np.empty((n_test_samples, n_initial_features + n_pattern_features), dtype=np.float32)
        X_test[:, :n_initial_features] = test_initial_features if test_initial_features is not None else 0.0
        for i, pattern in enumerate(self.pattern_list):
            series_idx = self.pattern_series_indices[i] if self.multiple_series and self.pattern_series_indices else None
            X_for_pattern = self.X_test[series_idx] if self.multiple_series and isinstance(self.X_test, list) and series_idx is not None else self.X_test
            X_data = np.asarray(X_for_pattern, dtype=np.float32) if not isinstance(X_for_pattern, np.ndarray) else X_for_pattern
            if self.multiple_series and series_idx is not None and X_data.ndim == 3:
                X_data = X_data[:, series_idx, :]
            start, end = self.pattern_starts[i], self.pattern_ends[i]
            X_region = X_data[:, start:end]
            pattern_feature = self.similarity_fn(X_region, pattern[start:end]).reshape(-1, 1)
            X_test[:, n_initial_features + i:n_initial_features + i+1] = pattern_feature
        result = {'patterns': self.pattern_list,'starts': self.pattern_starts,'ends': self.pattern_ends,'features': cached_features,'X_train': X_train,'X_val': X_val,'y_train': y_train,'y_val': y_val,'X_test': X_test}
        if self.multiple_series and self.pattern_series_indices: 
            result['series_indices'] = self.pattern_series_indices
        X_combined = np.vstack((X_train, X_val))
        y_combined = np.hstack((y_train, y_val))
        X_train, X_val, y_train, y_val = train_test_split(X_combined, y_combined, test_size=self.val_size, random_state=42)
        self.model.fit(X_train, y_train, X_val, y_val)
        result['model'] = self.model
        return result

    def save_parameters_to_json(self, dataset_name: Optional[str] = None) -> None:
        """
        Save all optimized pattern parameters to a JSON file.
        
        Parameters
        ----------
        dataset_name : str, optional
            Name of the dataset for file organization (default: uses self.dataset)
        """
        dataset_name = dataset_name or self.dataset
        params_dict = {
            'dataset': self.dataset,
            'metric': self.metric,
            'polynomial_degree': self.polynomial_degree,
            'n_patterns': len(self.pattern_list),
            'patterns': []
        }
        for i, pattern in enumerate(self.pattern_list):
            pattern_info = {
                'pattern_id': i,
                'pattern_start': int(self.pattern_starts[i]),
                'pattern_width': int(self.pattern_ends[i] - self.pattern_starts[i]),
                'pattern_values': pattern[self.pattern_starts[i]:self.pattern_ends[i]].tolist(),
            }
            if self.multiple_series and self.pattern_series_indices:
                pattern_info['series_index'] = int(self.pattern_series_indices[i])
            params_dict['patterns'].append(pattern_info)
        
        os.makedirs(f'json_files/{dataset_name}', exist_ok=True)
        with open(f'json_files/{dataset_name}/pattern_parameters.json', 'w') as f:
            json.dump(params_dict, f, indent=2)

    def visualize_patterns(
        self, 
        pattern_indices: Optional[List[int]] = None, 
        path: str = 'images/patterns.png',
        show_rmse_distribution: bool = True, 
        figsize: Optional[Tuple[int, int]] = None, 
        dpi: int = 300, 
        colors: Optional[Dict[str, str]] = None,
        save_image: bool = False,
        show_image: bool = True,
        title: Optional[str] = None,
        show_legend: bool = True,
        show_grid: bool = True,
        xlabel: Optional[str] = None,
        ylabel: Optional[str] = None
    ) -> None:
        """
        Visualize selected patterns and optionally save/show.
        
        Parameters
        ----------
        pattern_indices : list, optional
            List of pattern indices to visualize. If None, visualizes all patterns.
        path : str, optional
            Path for output file (default: 'images/patterns.png')
        show_rmse_distribution : bool, optional
            Whether to show RMSE distribution plot (default: True)
        figsize : tuple, optional
            Figure size (width, height). If None, auto-calculated.
        dpi : int, optional
            Resolution for saved image (default: 300)
        colors : dict, optional
            Custom colors {'pattern': color, 'active': color}
        save_image : bool, optional
            Whether to save image to file (default: False)
        show_image : bool, optional
            Whether to display image (default: True)
        title : str, optional
            Custom title prefix for each pattern plot
        show_legend : bool, optional
            Whether to show legend (default: True)
        show_grid : bool, optional
            Whether to show grid (default: True)
        xlabel : str, optional
            Custom x-axis label (default: 'Position')
        ylabel : str, optional
            Custom y-axis label (default: 'Pattern Value')
        """
        if pattern_indices is None:
            pattern_indices = list(range(len(self.pattern_list)))
            
        valid_indices = [i for i in pattern_indices if 0 <= i < len(self.pattern_list)]
        n_patterns = len(valid_indices)
        colors = colors or {'pattern': 'blue', 'active': 'red'}
        n_cols = 2 if show_rmse_distribution else 1
        figsize = figsize or (16 if show_rmse_distribution else 8, 4 * n_patterns)
        
        fig, axes = plt.subplots(n_patterns, n_cols, figsize=figsize)
        if n_patterns == 1:
            axes = axes.reshape(1, -1) if show_rmse_distribution else [axes]
        
        for idx, pattern_idx in enumerate(valid_indices):
            pattern = self.pattern_list[pattern_idx]
            start = self.pattern_starts[pattern_idx]
            end = self.pattern_ends[pattern_idx]
            
            ax_left = axes[idx, 0] if show_rmse_distribution else axes[idx]
            active_x = range(start, end)
            
            ax_left.plot(range(len(pattern)), pattern, color=colors['pattern'], alpha=0.3, label='Full Pattern')
            ax_left.plot(active_x, pattern[start:end], color=colors['active'], linewidth=3, label='Active Region')
            ax_left.scatter(active_x, pattern[start:end], c=colors['active'], s=50, zorder=5)
            
            plot_title = title or f"Pattern {pattern_idx} (positions {start}-{end})"
            if title is None and self.multiple_series and self.pattern_series_indices:
                plot_title += f", Series {self.pattern_series_indices[pattern_idx]}"
            ax_left.set_title(plot_title)
            ax_left.set_xlabel(xlabel or 'Position')
            ax_left.set_ylabel(ylabel or 'Pattern Value')
            if show_legend:
                ax_left.legend()
            if show_grid:
                ax_left.grid(True, alpha=0.3)
            
            if show_rmse_distribution:
                ax_right = axes[idx, 1]
                series_idx = self.pattern_series_indices[pattern_idx] if self.multiple_series and self.pattern_series_indices else None
                X_data = self.X_train[:, series_idx, :] if self.multiple_series and series_idx is not None else self.X_train
                X_region = X_data[:, start:end]
                rmse_values = self.similarity_fn(X_region, pattern[start:end].astype(np.float32)).flatten()
                
                has_hue = len(np.unique(self.y_train)) <= 10
                if has_hue:
                    sns.histplot(x=rmse_values, hue=self.y_train, bins=100, alpha=0.7, ax=ax_right)
                    ax_right.set_title('RMSE Distribution (by Target)')
                else:
                    sns.histplot(x=rmse_values, bins=100, alpha=0.7, ax=ax_right)
                    ax_right.set_title('RMSE Distribution')
                ax_right.set_xlabel('RMSE')
                ax_right.set_ylabel('Count')
                ax_right.grid(True, alpha=0.3)
        
        plt.tight_layout()
        if save_image:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            plt.savefig(path, dpi=dpi, bbox_inches='tight')
            print(f"Patterns visualized and saved to: {path}")
        if show_image:
            plt.show()
        else:
            plt.close(fig)

    def visualize_pattern_match(
        self, 
        sample_idx: int = 0, 
        pattern_idx: int = 0, 
        X_data: Optional[Union[NDArray[np.float32], List[NDArray[np.float32]]]] = None, 
        y_data: Optional[NDArray[np.float32]] = None, 
        path: str = 'images/pattern_match.png',
        figsize: Tuple[int, int] = (14, 8), 
        dpi: int = 300,
        save_image: bool = False,
        show_image: bool = True,
        title: Optional[str] = None,
        show_legend: bool = True,
        show_grid: bool = True,
        xlabel: Optional[str] = None,
        ylabel: Optional[str] = None,
        colors: Optional[Dict[str, str]] = None
    ) -> None:
        """
        Visualize how well a pattern matches a specific sample, showing similarity.
        
        Creates a two-panel visualization:
        - Top: Full time series with highlighted pattern region
        - Bottom: Zoomed comparison of data region vs. pattern
        
        Parameters
        ----------
        sample_idx : int, optional
            Index of sample to visualize (default: 0)
        pattern_idx : int, optional
            Index of pattern to visualize (default: 0)
        X_data : array-like or list, optional
            Data to use. If None, uses X_test.
        y_data : array-like, optional
            Labels for samples
        path : str, optional
            Path for output file (default: 'images/pattern_match.png')
        figsize : tuple, optional
            Figure size (default: (14, 8))
        dpi : int, optional
            Resolution (default: 300)
        save_image : bool, optional
            Whether to save image to file (default: False)
        show_image : bool, optional
            Whether to display image (default: True)
        title : str, optional
            Custom title for the plot
        show_legend : bool, optional
            Whether to show legend (default: True)
        show_grid : bool, optional
            Whether to show grid (default: True)
        xlabel : str, optional
            Custom x-axis label (default: 'Time Point')
        ylabel : str, optional
            Custom y-axis label (default: 'Signal Value')
        colors : dict, optional
            Custom colors {'data': color, 'pattern': color, 'region': color}
        """
        X_data = self.X_test if X_data is None else X_data
        
        pattern = self.pattern_list[pattern_idx]
        start, end = self.pattern_starts[pattern_idx], self.pattern_ends[pattern_idx]
        series_idx = self.pattern_series_indices[pattern_idx] if self.multiple_series and self.pattern_series_indices else None
        
        series_data = (X_data[series_idx][sample_idx] if self.multiple_series and series_idx is not None and isinstance(X_data, list)
                      else X_data[sample_idx] if not isinstance(X_data, list) else X_data[0][sample_idx])
        
        region, pattern_region = series_data[start:end], pattern[start:end]
        score = self.similarity_fn(region.reshape(1, -1), pattern_region)[0]
        
        pattern_scaled = ((pattern_region - pattern_region.mean()) / pattern_region.std() * region.std() + region.mean()
                         if pattern_region.std() > 0 else pattern_region + region.mean())
        
        colors = colors or {'data': '#2E86AB', 'pattern': '#A23B72', 'region': '#F18F01'}
        
        sns.set_style("whitegrid")
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figsize, height_ratios=[1, 1.2])
        
        ax1.plot(series_data, color=colors['data'], linewidth=2.5, alpha=0.8)
        ax1.axvspan(start, end-1, alpha=0.2, color=colors['region'], label='Pattern Region')
        ax1.set_ylabel(ylabel or 'Signal Value', fontsize=11, fontweight='bold')
        ax1.set_title(title or f"Sample {sample_idx} - Pattern {pattern_idx} Match" + 
                     (f" (Class: {int(y_data[sample_idx])})" if y_data is not None else ""), 
                     fontsize=13, fontweight='bold', pad=15)
        if show_legend:
            ax1.legend(loc='upper right', fontsize=10)
        if show_grid:
            ax1.grid(True, alpha=0.3, linestyle='--')
        ax1.set_xlim(-1, len(series_data))
        
        x_positions = np.arange(len(region))
        width = 0.35
        ax2.bar(x_positions - width/2, region, width, label='Actual Data', color=colors['data'], alpha=0.7, edgecolor='black', linewidth=1.2)
        ax2.bar(x_positions + width/2, pattern_scaled, width, label='Pattern (scaled)', color=colors['pattern'], alpha=0.7, edgecolor='black', linewidth=1.2)
        
        ax2.set_xlabel(xlabel or f'Position in Pattern Region ({start}-{end})', fontsize=11, fontweight='bold')
        ax2.set_ylabel(ylabel or 'Signal Value', fontsize=11, fontweight='bold')
        ax2.set_xticks(x_positions[::max(1, len(x_positions)//10)])
        ax2.set_xticklabels([str(start + i) for i in x_positions[::max(1, len(x_positions)//10)]])
        
        metric_name = 'RMSE' if 'rmse' in str(self.similarity_fn).lower() else 'Similarity Score'
        similarity_quality = 'Excellent' if score < 0.5 else 'Good' if score < 1.0 else 'Moderate' if score < 2.0 else 'Poor'
        textstr = f'{metric_name}: {score:.4f}\nMatch Quality: {similarity_quality}'
        ax2.text(0.98, 0.97, textstr, transform=ax2.transAxes, fontsize=11,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFF9E3', edgecolor='#333', linewidth=2, alpha=0.9))
        
        if show_legend:
            ax2.legend(loc='upper left', fontsize=10, framealpha=0.9)
        if show_grid:
            ax2.grid(True, alpha=0.3, linestyle='--', axis='y')
        
        plt.tight_layout()
        if save_image:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            plt.savefig(path, dpi=dpi, bbox_inches='tight')
        if show_image:
            plt.show()
        else:
            plt.close(fig)

    def visualize_decision_boundary(
        self, 
        pattern_idx1: int = 0, 
        pattern_idx2: int = 1, 
        features_data: Optional[NDArray[np.float32]] = None, 
        y_data: Optional[NDArray[np.float32]] = None, 
        path: str = 'images/decision_boundary.png', 
        resolution: float = 0.02, 
        figsize: Tuple[int, int] = (7, 6), 
        dpi: int = 300,
        save_image: bool = False,
        show_image: bool = True,
        title: Optional[str] = None,
        show_legend: bool = True,
        show_grid: bool = False,
        xlabel: Optional[str] = None,
        ylabel: Optional[str] = None,
        colors: Optional[List[str]] = None,
        marker: str = 'x',
        marker_size: int = 15,
        alpha_background: float = 0.6,
        alpha_points: float = 0.5
    ) -> None:
        """
        Visualize 2D decision boundary using two selected patterns.
        
        Parameters
        ----------
        pattern_idx1 : int, optional
            Index of first pattern (x-axis, default: 0)
        pattern_idx2 : int, optional
            Index of second pattern (y-axis, default: 1)
        features_data : array-like, optional
            Feature matrix. If None, uses training features.
        y_data : array-like, optional
            Labels. If None, uses y_train.
        path : str, optional
            Path for output file (default: 'images/decision_boundary.png')
        resolution : float, optional
            Grid resolution (default: 0.02)
        figsize : tuple, optional
            Figure size (default: (7, 6))
        dpi : int, optional
            Resolution (default: 300)
        save_image : bool, optional
            Whether to save image to file (default: False)
        show_image : bool, optional
            Whether to display image (default: True)
        title : str, optional
            Custom title for the plot
        show_legend : bool, optional
            Whether to show legend (default: True)
        show_grid : bool, optional
            Whether to show grid (default: False)
        xlabel : str, optional
            Custom x-axis label (default: 'RMSE of pattern X')
        ylabel : str, optional
            Custom y-axis label (default: 'RMSE of pattern Y')
        colors : list, optional
            List of colors for different classes
        marker : str, optional
            Marker style for scatter points (default: 'x')
        marker_size : int, optional
            Size of scatter markers (default: 15)
        alpha_background : float, optional
            Opacity of background decision regions (default: 0.6)
        alpha_points : float, optional
            Opacity of scatter points (default: 0.5)
        """
        features_data = features_data if features_data is not None else np.column_stack(self.features_list)
        y_data = y_data or self.y_train
        
        X_2d = np.column_stack([features_data[:, pattern_idx1], features_data[:, pattern_idx2]])
        x_min, x_max = X_2d[:, 0].min() - 0.05, X_2d[:, 0].max() + 0.05
        y_min, y_max = X_2d[:, 1].min() - 0.05, X_2d[:, 1].max() + 0.05
        
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
        mesh_points = np.c_[xx.ravel(), yy.ravel()]
        
        temp_model = clone_model(self.model)
        temp_model.fit(X_2d, y_data, None, None)
        Z = temp_model.predict(mesh_points).reshape(xx.shape)
        
        sns.set_style("whitegrid")
        fig, ax = plt.subplots(figsize=figsize)
        
        unique_classes = np.unique(y_data)
        n_classes = len(unique_classes)
        
        from matplotlib.colors import ListedColormap
        bg_colors = colors or ['lightblue', 'lightcoral', 'lightgreen', 'lightsalmon', 'plum']
        bg_cmap = ListedColormap(bg_colors[:n_classes])
        point_colors = colors or ['blue', 'red', 'green', 'orange', 'purple']
        
        ax.contourf(xx, yy, Z, levels=n_classes - 1, cmap=bg_cmap, alpha=alpha_background, zorder=2)
        
        for i, cls in enumerate(unique_classes):
            mask = y_data == cls
            ax.scatter(X_2d[mask, 0], X_2d[mask, 1], c=point_colors[i % len(point_colors)], 
                      label=f'Class {int(cls)}', marker=marker, s=marker_size, 
                      alpha=alpha_points, zorder=4, linewidth=1)
        
        ax.set_xlabel(xlabel or f'RMSE of pattern {pattern_idx1}')
        ax.set_ylabel(ylabel or f'RMSE of pattern {pattern_idx2}')
        ax.set_title(title or f'Decision Boundary: Pattern {pattern_idx1} vs Pattern {pattern_idx2}')
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        if show_legend:
            ax.legend()
        if show_grid:
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        if save_image:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            plt.savefig(path, dpi=dpi, bbox_inches='tight')
        if show_image:
            plt.show()
        else:
            plt.close(fig)
