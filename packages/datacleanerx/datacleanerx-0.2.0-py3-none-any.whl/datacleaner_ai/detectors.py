import pandas as pd
import numpy as np

def detect_missing(df):
    """Detect missing values per column and overall."""
    missing_per_col = df.isnull().sum()
    total_missing = missing_per_col.sum()
    total_cells = df.size
    percent_missing = (total_missing / total_cells) * 100

    return {
        'missing_per_column': missing_per_col.to_dict(),
        'total_missing': int(total_missing),
        'percent_missing': round(percent_missing, 2)
    }

def detect_duplicates(df):
    """Count duplicate rows."""
    return int(df.duplicated().sum())

def detect_imbalance(df, target_column):
    """Detect class distribution for classification target."""
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in DataFrame.")

    value_counts = df[target_column].value_counts()
    minority_class = value_counts.min()
    majority_class = value_counts.max()
    ratio = minority_class / majority_class

    return {
        'class_distribution': value_counts.to_dict(),
        'imbalance_ratio': round(ratio, 3),
        'is_imbalanced': ratio < 0.5  # Arbitrary threshold
    }

def detect_outliers(df, method="iqr"):
    """Detect outliers using IQR or Z-score (numeric cols only)."""
    outlier_info = {}
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        if method == "iqr":
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        elif method == "zscore":
            mean = df[col].mean()
            std = df[col].std()
            z_scores = (df[col] - mean) / std
            outliers = df[z_scores.abs() > 3]
        else:
            raise ValueError("Method must be 'iqr' or 'zscore'")

        outlier_info[col] = {
            'count': len(outliers),
            'percent': round(len(outliers) / len(df) * 100, 2)
        }
    return outlier_info