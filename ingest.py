from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
RAW_FILE = BASE_DIR / "data" / "raw" / "faostat_africa_raw.csv"

EXPECTED_COLUMNS = ["Area", "Item", "Element", "Unit", "Y2023"]


def ingest():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw file not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE, encoding="utf-8")

    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

    print(f"Rows: {len(df)}")
    print(f"Columns: {df.shape[1]}")
    print(f"Countries: {df['Area'].nunique()}")
    print(f"Items: {df['Item'].nunique()}")
    return df


if __name__ == "__main__":
    ingest()