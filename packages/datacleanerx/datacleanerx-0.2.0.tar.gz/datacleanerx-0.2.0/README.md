# DataCleanerX

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.1-blue.svg)](https://pypi.org/project/datacleanerx/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**DataCleanerX** is an intelligent Python library that automates the data preprocessing pipeline for machine learning projects. Spend less time cleaning data and more time building models.

## 🚀 Quick Start

```bash
pip install datacleanerx==0.1.1
```

```python
from datacleanerx import Cleaner
import pandas as pd

# Load your data
df = pd.read_csv("data.csv")

# Clean in one line
cleaner = Cleaner(strategy="auto")
df_clean = cleaner.fit_transform(df)

# View cleaning report
print(cleaner.report())
```

## ✨ Features

DataCleanerX automatically detects and resolves common data quality issues:

### Detection Capabilities
- **Missing Values** - Identifies null, NaN, and empty entries
- **Duplicate Rows** - Finds exact and near-duplicate records
- **Class Imbalance** - Detects imbalanced target distributions
- **Outliers** - Identifies statistical anomalies using Z-score or IQR methods

### Cleaning Operations
- **Missing Data Handling** - Drop, mean/median imputation, forward/backward fill
- **Deduplication** - Removes duplicate entries while preserving data integrity
- **Class Balancing** - SMOTE oversampling, random under/oversampling
- **Outlier Treatment** - Clipping, removal, or replacement strategies

### Reporting
- Comprehensive summary of all detected issues
- Actionable insights on cleaning operations performed
- Statistics on data quality improvements

## 📖 Why DataCleanerX?

Data scientists spend 60-80% of their time on data cleaning before model training. DataCleanerX addresses this by:

- **Automating repetitive tasks** - One-line data cleaning with intelligent defaults
- **Preventing common mistakes** - Catches issues beginners often miss
- **Maintaining flexibility** - Fully customizable strategies for advanced users
- **Providing transparency** - Detailed reports on all operations performed

## 🎯 Use Cases

- **Rapid Prototyping** - Quickly clean datasets for exploratory analysis
- **Production Pipelines** - Integrate into automated ML workflows
- **Educational Projects** - Learn data cleaning best practices
- **Competition Prep** - Fast preprocessing for Kaggle competitions

## 📚 Documentation

### Basic Usage

```python
from datacleanerx import Cleaner
import pandas as pd

df = pd.read_csv("messy_data.csv")

# Automatic cleaning with defaults
cleaner = Cleaner(strategy="auto")
df_clean = cleaner.fit_transform(df)
```

### Custom Configuration

```python
# Fine-tune cleaning strategies
cleaner = Cleaner(
    strategy="manual",
    missing_values="median",
    duplicates=True,
    imbalance="smote",
    outliers="clip"
)

df_clean = cleaner.fit_transform(df, target_column="label")
print(cleaner.report())
```

### API Reference

#### `Cleaner` Class

**Parameters:**
- `strategy` (str): `"auto"` or `"manual"` - Cleaning approach
- `missing_values` (str): `"drop"`, `"mean"`, `"median"`, `"ffill"`, `"bfill"`
- `duplicates` (bool): Whether to remove duplicate rows
- `imbalance` (str): `"smote"`, `"oversample"`, `"undersample"`, or `None`
- `outliers` (str): `"clip"`, `"remove"`, or `None`

**Methods:**
- `fit(df)` - Analyze dataset and identify issues
- `transform(df)` - Apply cleaning operations
- `fit_transform(df)` - Analyze and clean in one step
- `report()` - Generate detailed cleaning summary

### Example Report Output

```text
=== DataCleanerX Cleaning Report ===
Dataset: 10,000 rows × 15 columns

Issues Detected:
✓ Missing values: 12.3% (1,845 cells)
✓ Duplicate rows: 350 (3.5%)
✓ Class imbalance: 1:7 ratio detected
✓ Outliers: 2.3% (345 values)

Actions Taken:
→ Missing values: Median imputation applied
→ Duplicates: 350 rows removed
→ Class balance: SMOTE oversampling (minority class: 1,200 → 6,850)
→ Outliers: Clipped using IQR method

Final Dataset: 9,650 rows × 15 columns
====================================
```

## 🏗️ Architecture

```
datacleanerx/
├── cleaner.py          # Main Cleaner class
├── detectors.py        # Issue detection functions
├── transformers.py     # Data cleaning operations
├── reports.py          # Report generation
└── utils.py            # Helper utilities
```

## 🛠️ Advanced Features

### Integration with Scikit-learn for future version

```python
from sklearn.pipeline import Pipeline
from datacleanerx import Cleaner
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('cleaner', Cleaner(strategy="auto")),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
```

### Handling Specific Data Types

```python
# For time series data
cleaner = Cleaner(missing_values="ffill")

# For categorical data
cleaner = Cleaner(missing_values="mode")

# For mixed data types
cleaner = Cleaner(strategy="auto")  # Automatically detects types
```

## 📦 Dependencies

**Core Requirements:**
- pandas >= 1.0.0
- numpy >= 1.18.0

**Optional (for advanced features):**
- imbalanced-learn >= 0.8.0 (for SMOTE)
- scikit-learn >= 0.24.0 (for pipeline integration)

## 🧪 Development

### Running Tests

```bash
git clone https://github.com/SatyamSingh8306/datacleanerx.git
cd datacleanerx
pip install -e ".[dev]"
pytest tests/
```

### Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Roadmap

### Version 0.2.0 (Upcoming)
- [ ] Visualization tools (missing value heatmaps, distribution plots)
- [ ] Save/load cleaning configurations as JSON
- [ ] Enhanced outlier detection algorithms
- [ ] Support for text data preprocessing

### Version 0.3.0 (Future)
- [ ] CLI tool for non-Python users
- [ ] Parallel processing for large datasets
- [ ] Auto-tuning of cleaning strategies
- [ ] Integration with popular ML frameworks

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with inspiration from the data science community's need for faster, more reliable preprocessing tools.

## 📧 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/SatyamSingh8306/datacleanerx/issues)
- **Discussions**: [GitHub Discussions](https://github.com/SatyamSingh8306/datacleanerx/discussions)
- **Email**: satyamsingh7734@gmail.com

---

**Made with Satyam Singh**

*Star ⭐ this repo if you find it useful!*