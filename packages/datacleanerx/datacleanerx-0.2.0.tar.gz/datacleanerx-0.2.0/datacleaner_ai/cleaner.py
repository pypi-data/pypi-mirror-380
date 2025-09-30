import pandas as pd
from .detectors import detect_missing, detect_duplicates, detect_imbalance, detect_outliers
from .transformers import handle_missing, remove_duplicates, balance_classes, handle_outliers
from .reports import generate_report

class Cleaner:
    """
    Main class for automated dataset cleaning for ML.
    """

    def __init__(self, strategy="auto", missing_values="median", duplicates=True,
                 imbalance=None, outliers=None, target_column=None):
        self.strategy = strategy
        self.missing_values = missing_values
        self.duplicates = duplicates
        self.imbalance = imbalance
        self.outliers = outliers
        self.target_column = target_column
        self.report_data = {}

    def fit(self, df):
        """Analyze the dataset and store detected issues."""
        print("🔍 Detecting data quality issues...")

        # Detect issues
        self.report_data['missing'] = detect_missing(df)
        self.report_data['duplicates'] = detect_duplicates(df)
        if self.target_column:
            self.report_data['imbalance'] = detect_imbalance(df, self.target_column)
        self.report_data['outliers'] = detect_outliers(df)

        return self

    def transform(self, df):
        """Apply cleaning transformations based on configuration."""
        print("🧹 Applying cleaning transformations...")

        # Handle missing values
        if self.report_data.get('missing', {}).get('total_missing', 0) > 0:
            df = handle_missing(df, method=self.missing_values)
            self.report_data['missing']['handled_by'] = self.missing_values

        # Remove duplicates
        if self.duplicates and self.report_data.get('duplicates', 0) > 0:
            original_len = len(df)
            df = remove_duplicates(df)
            removed = original_len - len(df)
            self.report_data['duplicates'] = removed

        # Balance classes (if target provided)
        if self.imbalance and self.target_column:
            df = balance_classes(df, self.target_column, method=self.imbalance)
            self.report_data['imbalance']['handled_by'] = self.imbalance

        # Handle outliers
        if self.outliers:
            df = handle_outliers(df, method=self.outliers)
            self.report_data['outliers']['handled_by'] = self.outliers

        return df

    def fit_transform(self, df):
        """Convenience method to fit and transform in one step."""
        return self.fit(df).transform(df)

    def report(self):
        """Generate and return a human-readable summary report."""
        return generate_report(self.report_data)