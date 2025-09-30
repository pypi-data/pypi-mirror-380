import pandas as pd
from datacleaner_ai import Cleaner

def test_cleaner_basic():
    data = {
        'A': [1, 2, None, 4, 2],
        'B': [5, 6, 7, 8, 6],
        'C': ['x', 'y', 'x', 'z', 'y']
    }
    df = pd.DataFrame(data)

    cleaner = Cleaner(missing_values="mean", duplicates=True)
    df_clean = cleaner.fit_transform(df)

    assert df_clean.isnull().sum().sum() == 0, "Missing values not handled"
    assert len(df_clean) < len(df), "Duplicates not removed"

    report = cleaner.report()
    assert "Missing values" in report
    assert "Duplicates" in report

    print("✅ All tests passed!")