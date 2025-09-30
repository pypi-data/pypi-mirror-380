import pandas as pd
from sklearn.utils import resample

def handle_missing(df, method="median"):
    """Handle missing values with specified strategy."""
    df_clean = df.copy()

    if method == "drop":
        df_clean = df_clean.dropna()
    else:
        for col in df_clean.columns:
            if df_clean[col].dtype in ['float64', 'int64']:
                if method == "mean":
                    df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
                elif method == "median":
                    df_clean[col] = df_clean[col].fillna(df_clean[col].median())
            else:
                if method in ["ffill", "bfill"]:
                    df_clean[col] = df_clean[col].fillna(method=method)
                else:
                    # Default for non-numeric: fill with mode or placeholder
                    mode_val = df_clean[col].mode()
                    fill_val = mode_val[0] if len(mode_val) > 0 else "Unknown"
                    df_clean[col] = df_clean[col].fillna(fill_val)

    return df_clean

def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates().reset_index(drop=True)

def balance_classes(df, target_column, method="oversample"):
    """Balance target classes using simple resampling (SMOTE later)."""
    if method == "undersample":
        # Undersample majority class
        min_class_count = df[target_column].value_counts().min()
        df_balanced = df.groupby(target_column).apply(lambda x: x.sample(min_class_count)).reset_index(drop=True)
    elif method == "oversample":
        # Oversample minority class(es)
        max_class_count = df[target_column].value_counts().max()
        dfs = []
        for cls in df[target_column].unique():
            subset = df[df[target_column] == cls]
            if len(subset) < max_class_count:
                subset = resample(subset, replace=True, n_samples=max_class_count, random_state=42)
            dfs.append(subset)
        df_balanced = pd.concat(dfs).sample(frac=1, random_state=42).reset_index(drop=True)
    else:
        raise ValueError("Method must be 'oversample' or 'undersample' for MVP.")

    return df_balanced

def handle_outliers(df, method="clip"):
    """Handle outliers by clipping or removal (IQR-based)."""
    df_clean = df.copy()
    numeric_cols = df_clean.select_dtypes(include=['number']).columns

    for col in numeric_cols:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        if method == "clip":
            df_clean[col] = df_clean[col].clip(lower=lower_bound, upper=upper_bound)
        elif method == "remove":
            df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]

    return df_clean.reset_index(drop=True)