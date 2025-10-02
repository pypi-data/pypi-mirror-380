# PatX - Pattern eXtraction for Time Series Feature Engineering

[![PyPI version](https://badge.fury.io/py/patx.svg)](https://badge.fury.io/py/patx)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

PatX is a Python package for extracting polynomial patterns from time series data to create meaningful features for machine learning models. It uses Optuna optimization to automatically discover patterns that are most predictive for your target variable.

## Scientific Background

Time series pattern extraction is a fundamental challenge in computational biology, signal processing, and data mining. PatX addresses the critical need for automated feature engineering in temporal data by discovering locally optimal polynomial patterns that maximize predictive performance. The package implements a novel optimization-based approach that combines:

- **Automated Pattern Discovery**: Leverages Bayesian optimization to efficiently explore the space of possible patterns
- **Multi-scale Analysis**: Extracts patterns at different temporal scales and locations within time series
- **Feature Engineering**: Transforms raw temporal data into discriminative similarity-based features
- **Cross-validation Integration**: Ensures robust pattern selection through validation-based optimization

## Applications

PatX has been successfully applied across diverse domains:

**Computational Biology & Bioinformatics:**
- Epigenomic signal analysis (ChIP-seq, ATAC-seq)
- Gene expression time course analysis
- Protein structure prediction from sequence data
- Biomarker discovery in clinical time series

**Signal Processing & Engineering:**
- Anomaly detection in sensor networks
- Quality control in manufacturing processes
- Predictive maintenance from vibration signals
- Speech and audio pattern recognition

**Finance & Economics:**
- Market trend identification
- Risk assessment from trading patterns
- Economic indicator forecasting
- Algorithmic trading signal generation

**Healthcare & Medical Informatics:**
- ECG pattern classification for arrhythmia detection
- EEG analysis for neurological disorders
- Patient monitoring and early warning systems
- Drug response prediction from temporal biomarkers

## Features

- **Automatic Pattern Discovery**: Uses optimization to find the most predictive polynomial patterns in your time series data
- **Multiple Series Support**: Handle datasets with multiple time series channels
- **Flexible Models**: Built-in support for LightGBM with easy extension to custom models
- **Rich Visualizations**: Visualize patterns, test samples, and decision boundaries
- **Customizable**: Bring your own pattern functions and similarity metrics
- **Easy Integration**: Simple API that works with scikit-learn workflows

## Installation

```bash
pip install patx
```

## Quick Start

Copy and paste this complete example to get started immediately:

```python
import numpy as np
from patx import PatternExtractor, load_remc_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# Load the included REMC dataset with two time series (H3K4me3, H3K4me1)
data = load_remc_data(series=("H3K4me3", "H3K4me1"))
X_list = data['X_list']  # list of np arrays, one per series
y = data['y']
series_names = data['series_names']

print(f"Loaded {len(X_list)} series: {series_names}")
print(f"Samples: {len(y)}, time points per series: {X_list[0].shape[1]}")  # 40 time points (binned for lightweight package)

# Split indices, then slice each series list (multiple time series)
indices = np.arange(len(y))
train_indices, test_indices = train_test_split(
    indices, test_size=0.3, random_state=42, stratify=y
)

X_train_list = [X[train_indices] for X in X_list]
X_test_list = [X[test_indices] for X in X_list]
y_train, y_test = y[train_indices], y[test_indices]

# Create PatternExtractor (automatically detects multiple series)
optimizer = PatternExtractor(
    X_train=X_train_list,
    y_train=y_train,
    X_test=X_test_list
)

# Extract features and train model
result = optimizer.feature_extraction()

# Get results
trained_model = result['model']
patterns = result['patterns']
test_probabilities = trained_model.predict_proba_positive(result['X_test'])

# Evaluate performance
auc_score = roc_auc_score(y_test, test_probabilities)
print(f"\nResults:")
print(f"Discovered {len(patterns)} patterns across {len(X_list)} time series")
print(f"Test AUC: {auc_score:.4f}")

# Visualize patterns
optimizer.visualize_patterns(save_image=True, show_image=False, path='images/patterns.png')
print("Pattern visualizations saved!")
```

### Visualization Examples

PatX offers three powerful visualization functions:

#### 1. Visualize Patterns

```python
# Display all patterns interactively (default behavior)
optimizer.visualize_patterns()

# Save patterns to file
optimizer.visualize_patterns(save_image=True, show_image=False, path='images/patterns.png')

# Customize visualization
optimizer.visualize_patterns(
    pattern_indices=[0, 1, 2],
    save_image=True,
    show_image=False,
    path='images/custom_patterns.png',
    colors={'pattern': 'purple', 'active': 'orange'},
    show_rmse_distribution=False,
    title='Custom Pattern',
    xlabel='Position (bp)',
    ylabel='Signal Intensity'
)
```

#### 2. Visualize Pattern Match

Shows how well a pattern matches a specific sample with a clear two-panel view:

```python
# Display pattern match interactively (uses first sample and first pattern by default)
optimizer.visualize_pattern_match()

# Save to file with customization
optimizer.visualize_pattern_match(
    sample_idx=5,
    pattern_idx=0,
    X_data=X_test_list,
    y_data=y_test,
    save_image=True,
    show_image=False,
    path='images/pattern_match_sample_5.png',
    title='Custom Pattern Match Analysis',
    xlabel='Genomic Position',
    ylabel='ChIP-seq Signal',
    colors={'data': '#1f77b4', 'pattern': '#d62728', 'region': '#ff7f0e'}
)
```

#### 3. Visualize Decision Boundary

Shows 2D decision boundary using two patterns (defaults to first two patterns):

```python
# Display decision boundary interactively (uses patterns 0 and 1 by default)
optimizer.visualize_decision_boundary()

# Save with customization
optimizer.visualize_decision_boundary(
    pattern_idx1=0,
    pattern_idx2=1,
    save_image=True,
    show_image=False,
    path='images/decision_boundary.png',
    title='Classification Decision Boundary',
    xlabel='Pattern 1 Similarity (RMSE)',
    ylabel='Pattern 2 Similarity (RMSE)',
    marker='x',
    marker_size=20,
    alpha_background=0.5,
    alpha_points=0.6
)
```


### Convenience Features

PatternExtractor includes Pythonic convenience methods for easy access:

```python
from patx import PatternExtractor

# After extracting patterns
optimizer = PatternExtractor(X_train, y_train, X_test)
result = optimizer.feature_extraction()

# Get number of patterns
print(len(optimizer))  # or optimizer.n_patterns
# Output: 5

# String representation
print(optimizer)
# Output: PatternExtractor(dataset='default', patterns=5, metric='auc')

# Access individual patterns by index
pattern_info = optimizer[0]  # Get first pattern
print(pattern_info)
# Output: {'pattern': array([...]), 'start': 10, 'end': 25, 'series_index': 0}

# Iterate over all patterns
for i, pattern_info in enumerate(optimizer):
    print(f"Pattern {i}: start={pattern_info['start']}, end={pattern_info['end']}")

# Access all patterns
all_patterns = optimizer.patterns  # Returns list of pattern arrays

# Save parameters (uses dataset name by default)
optimizer.save_parameters_to_json()  # saves to json_files/default/
optimizer.save_parameters_to_json('my_experiment')  # custom name
```

### Custom Pattern and Similarity Functions

You can provide custom pattern generation functions and similarity metrics:

```python
import numpy as np
from patx import PatternExtractor

# Define custom pattern function (logarithmic)
def log_pattern(coeffs, n_points):
    x = np.linspace(1, n_points, n_points, dtype=np.float32)
    return coeffs[0] * np.log(x) + coeffs[1]

# Define custom similarity function (cosine similarity)
def cosine_similarity(X_region, pattern_values):
    norms = np.linalg.norm(X_region, axis=1) * np.linalg.norm(pattern_values)
    dots = np.dot(X_region, pattern_values)
    return 1 - (dots / (norms + 1e-10))

# Use custom functions
optimizer = PatternExtractor(
    X_train=X_train,
    y_train=y_train,
    dataset='MyDataset',
    X_test=X_test,
    pattern_fn=log_pattern,           # Custom pattern generation
    similarity_fn=cosine_similarity   # Custom similarity metric
)

result = optimizer.feature_extraction()
print(f"Extracted {len(result['patterns'])} patterns with custom functions")
```

**Pattern Function Signature:**
- Input: `coeffs` (list of coefficients), `n_points` (int)
- Output: 1D numpy array of length `n_points`
- Default: polynomial pattern

**Similarity Function Signature:**
- Input: `X_region` (2D array: samples × time points), `pattern_values` (1D array)
- Output: 1D array of similarity scores per sample
- Default: RMSE (lower is more similar)

## API Reference

### PatternExtractor

The main class for pattern extraction.

After calling `feature_extraction()`, the extractor stores:

- `patterns`: list of 1D numpy arrays (length = time points), each the discovered pattern, with active region filled and rest zeros
- `starts` / `ends`: start and end indices for each pattern’s active region
- `series_indices` (when multiple series): which series a pattern was optimized on
- `features`: cached training feature matrix built from discovered patterns (and optional initial features)
- `X_test`: feature matrix for the provided test data (aligned to `features` columns)
- `model`: the trained model refit on the final feature set

Return value of `feature_extraction()` is a dict exposing the same keys for convenience.

**Parameters:**
- `X_train`: Training time series data (array or list of arrays for multiple series)
- `y_train`: Training targets
- `dataset`: Dataset name
- `X_test`: Test data for feature extraction (same structure as `X_train`)
- `model`: Optional model instance (defaults to LightGBM based on task)
- `max_n_trials`: Optional max optimization trials (default: 50)
- `n_jobs`: Optional number of parallel jobs (default: -1)
- `show_progress`: Optional progress bar (default: True)
- `multiple_series`: Optional; inferred when `X_train` is a list
- `metric`: Optional; inferred (binary→auc, multiclass→accuracy, regression→rmse)
- `polynomial_degree`: Optional degree of polynomial patterns (default: 3)
- `val_size`: Optional validation split ratio (default: 0.3)
- `initial_features`: Optional initial features
- `pattern_fn`: Optional custom pattern generation function (default: polynomial_pattern)
- `similarity_fn`: Optional custom similarity calculation function (default: calculate_pattern_rmse)

**Properties:**
- `n_patterns`: Number of extracted patterns (same as `len(extractor)`)
- `patterns`: List of all extracted pattern arrays

**Convenience Methods:**
- `__len__()`: Returns number of extracted patterns
- `__str__()`: Human-readable representation
- `__repr__()`: Developer-friendly representation
- `__getitem__(idx)`: Access pattern by index, returns dict with 'pattern', 'start', 'end', 'series_index'
- `__iter__()`: Iterate over all patterns

**Methods:**
- `feature_extraction()`: Extract patterns and return features
- `save_parameters_to_json(dataset_name=None)`: Save pattern parameters (default: uses self.dataset)
- `visualize_patterns(pattern_indices, path, show_rmse_distribution, figsize, dpi, colors, save_image, show_image, title, show_legend, show_grid, xlabel, ylabel)`: Visualize discovered patterns
  - `pattern_indices`: List of pattern indices (default: all)
  - `path`: Output file path (default: 'images/patterns.png')
  - `show_rmse_distribution`: Show distribution plot (default: True)
  - `figsize`: Custom figure size (default: auto)
  - `dpi`: Resolution (default: 300)
  - `colors`: Custom colors dict `{'pattern': color, 'active': color}` (default: blue/red)
  - `save_image`: Save to file (default: False)
  - `show_image`: Display interactively (default: True)
  - `title`: Custom title (optional)
  - `show_legend`: Show legend (default: True)
  - `show_grid`: Show grid (default: True)
  - `xlabel`: X-axis label (default: 'Position')
  - `ylabel`: Y-axis label (default: 'Pattern Value')
- `visualize_pattern_match(sample_idx, pattern_idx, X_data, y_data, path, figsize, dpi, save_image, show_image, title, show_legend, show_grid, xlabel, ylabel, colors)`: Visualize how well a pattern matches a sample
  - `sample_idx`: Index of sample to visualize (default: 0)
  - `pattern_idx`: Index of pattern to show (default: 0)
  - `X_data`: Test data (default: uses X_test)
  - `y_data`: Labels for samples (optional)
  - `path`: Output file path (default: 'images/pattern_match.png')
  - `figsize`: Figure size (default: (14, 8))
  - `dpi`: Resolution (default: 300)
  - `save_image`: Save to file (default: False)
  - `show_image`: Display interactively (default: True)
  - `title`: Custom title (optional)
  - `show_legend`: Show legend (default: True)
  - `show_grid`: Show grid (default: True)
  - `xlabel`: X-axis label (default: 'Time Point')
  - `ylabel`: Y-axis label (default: 'Signal Value')
  - `colors`: Custom colors dict `{'data': color, 'pattern': color, 'region': color}`
- `visualize_decision_boundary(pattern_idx1, pattern_idx2, features_data, y_data, path, resolution, figsize, dpi, save_image, show_image, title, show_legend, show_grid, xlabel, ylabel, colors, marker, marker_size, alpha_background, alpha_points)`: Visualize 2D decision boundary
  - `pattern_idx1`: First pattern index (x-axis, default: 0)
  - `pattern_idx2`: Second pattern index (y-axis, default: 1)
  - `features_data`: Feature matrix (default: training features)
  - `y_data`: Labels (default: y_train)
  - `path`: Output file path (default: 'images/decision_boundary.png')
  - `resolution`: Grid resolution (default: 0.02)
  - `figsize`: Figure size (default: (7, 6))
  - `dpi`: Resolution (default: 300)
  - `save_image`: Save to file (default: False)
  - `show_image`: Display interactively (default: True)
  - `title`: Custom title (optional)
  - `show_legend`: Show legend (default: True)
  - `show_grid`: Show grid (default: False)
  - `xlabel`: X-axis label (default: 'RMSE of pattern X')
  - `ylabel`: Y-axis label (default: 'RMSE of pattern Y')
  - `colors`: List of colors for classes (optional)
  - `marker`: Marker style (default: 'x')
  - `marker_size`: Marker size (default: 15)
  - `alpha_background`: Background opacity (default: 0.6)
  - `alpha_points`: Points opacity (default: 0.5)

### Models

Built-in model support:
- `get_model(task_type, dataset, n_classes)`: Get configured LightGBM model
  - `task_type`: 'classification' or 'regression'
  - `dataset`: Dataset name for parameter optimization
  - `n_classes`: Number of classes (for multiclass classification)
- `LightGBMModel`: LightGBM wrapper with consistent interface
- `evaluate_model_performance(model, X, y, metric)`: Evaluate model

**Examples:**
```python
# Binary classification
model = get_model('classification', 'REMC')

# Multiclass classification
model = get_model('classification', 'MyDataset', n_classes=5)

# Regression
model = get_model('regression', 'MyDataset')
```

### Data

- `load_remc_data(series)`: Load the included REMC epigenomics dataset (multiple time series)

### Custom Models

You can use any model that implements `fit()` and `predict()` methods. Here's an example with sklearn:

**Sklearn Classifier Example:**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.base import clone

class SklearnClassifierWrapper:
    def __init__(self, sklearn_model):
        self.sklearn_model = sklearn_model
    
    def fit(self, X_train, y_train, X_val=None, y_val=None):
        self.sklearn_model.fit(X_train, y_train)
        return self
    
    def predict(self, X):
        return self.sklearn_model.predict(X)
    
    def predict_proba_positive(self, X):
        proba = self.sklearn_model.predict_proba(X)
        return proba[:, 1] if proba.ndim == 2 else proba
    
    def clone(self):
        return SklearnClassifierWrapper(clone(self.sklearn_model))

# Use custom model
base_model = LogisticRegression(max_iter=1000, random_state=42)
model = SklearnClassifierWrapper(base_model)
optimizer = PatternExtractor(X_train, y_train, X_test, model=model)
```

This wrapper works with any sklearn classifier (RandomForest, SVM, etc.).

## Future Directions

PatX continues to evolve with several exciting research directions:

**Algorithmic Enhancements:**
- **Deep Learning Integration**: Incorporating neural pattern extractors alongside polynomial functions
- **Multi-resolution Analysis**: Wavelet-based pattern discovery for complex temporal structures
- **Causal Pattern Mining**: Identifying causal relationships in temporal sequences
- **Online Learning**: Real-time pattern adaptation for streaming data

**Methodological Extensions:**
- **Non-parametric Patterns**: Support for spline-based and kernel-based pattern functions
- **Ensemble Methods**: Combining multiple pattern extraction strategies
- **Uncertainty Quantification**: Bayesian approaches for pattern reliability assessment
- **Transfer Learning**: Cross-domain pattern knowledge transfer

**Domain-Specific Applications:**
- **Climate Science**: Extreme weather pattern detection and prediction
- **Neuroscience**: Brain connectivity pattern analysis from fMRI/EEG data
- **Materials Science**: Property prediction from molecular dynamics trajectories
- **Social Networks**: Temporal behavior pattern mining in social media data

**Performance & Scalability:**
- **Distributed Computing**: Spark/Dask integration for large-scale datasets
- **GPU Acceleration**: CUDA-based pattern optimization
- **Memory Optimization**: Streaming algorithms for massive time series
- **Approximate Methods**: Fast approximate pattern matching for real-time applications

## Contributing

Contributions are welcome! We particularly encourage contributions in:
- New pattern generation functions
- Domain-specific similarity metrics
- Visualization enhancements
- Performance optimizations
- Documentation and tutorials

Please feel free to submit a Pull Request or open an issue for discussion.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use PatX in your research, please cite:

```bibtex
@software{patx,
  title={PatX: Pattern eXtraction for Time Series Feature Engineering},
  author={Wolber, J.},
  year={2025},
  url={https://github.com/Prgrmmrjns/patX}
}
```

## References

PatX builds upon established research in time series analysis and pattern mining:

- Bayesian optimization for hyperparameter tuning (Snoek et al., 2012)
- Time series feature extraction methodologies (Christ et al., 2018)
- Polynomial pattern matching in biological sequences (Durbin et al., 1998)
- Multi-scale temporal pattern analysis (Fulcher & Jones, 2017)

For detailed algorithmic descriptions and performance benchmarks, see the accompanying research paper (in preparation).