def generate_report(report_data):
    """Generate a human-readable summary report."""
    lines = []
    lines.append("=== 🧹 Dataset Cleaner Report ===")

    # Missing values
    missing = report_data.get('missing', {})
    if missing.get('total_missing', 0) > 0:
        handled_by = missing.get('handled_by', 'Not handled')
        lines.append(f"Missing values: {missing['percent_missing']}% ({missing['total_missing']} cells) → Handled by: {handled_by}")
    else:
        lines.append("No missing values detected.")

    # Duplicates
    duplicates = report_data.get('duplicates', 0)
    if duplicates > 0:
        lines.append(f"Duplicates: {duplicates} rows removed.")
    else:
        lines.append("No duplicate rows detected.")

    # Imbalance
    imbalance = report_data.get('imbalance', {})
    if imbalance.get('is_imbalanced'):
        handled_by = imbalance.get('handled_by', 'Not handled')
        ratio = imbalance.get('imbalance_ratio', 0)
        lines.append(f"Class imbalance detected (ratio: {ratio}) → Handled by: {handled_by}")
    elif imbalance:
        lines.append("Classes are balanced.")

   # Outliers
    outliers = report_data.get('outliers', {})
    handled_by = report_data.get('outliers_handled_by', 'Not handled')

    if isinstance(outliers, dict):
        # Only sum over column dicts, ignore any non-dict entries (shouldn't exist now)
        outlier_counts = [info.get('count', 0) for info in outliers.values() if isinstance(info, dict)]
        outlier_percents = [info.get('percent', 0) for info in outliers.values() if isinstance(info, dict)]
        total_outliers = sum(outlier_counts)
        avg_pct = sum(outlier_percents) / len(outlier_percents) if outlier_percents else 0
    else:
        total_outliers = 0
        avg_pct = 0

    if total_outliers > 0:
        lines.append(f"Outliers detected: ~{round(avg_pct, 2)}% across columns → Handled by: {handled_by}")
    else:
        lines.append("No significant outliers detected.")

    lines.append("===============================")
    return "\n".join(lines)