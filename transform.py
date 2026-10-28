from pathlib import Path
import pandas as pd

from ingest import ingest

BASE_DIR = Path(__file__).resolve().parent
CLEAN_DIR = BASE_DIR / "data" / "clean"
CLEAN_FILE = CLEAN_DIR / "livestock_long.csv"

ITEMS = [
    "Meat of cattle with the bone, fresh or chilled",
    "Meat of chickens, fresh or chilled",
    "Hen eggs in shell, fresh",
]


def transform(df):
    # 1. Keep only the livestock items we care about
    df = df[df["Item"].isin(ITEMS)]

    # 2. Find the year columns (Y1961, Y1962, ...) but not the flag/note columns
    year_cols = [c for c in df.columns if c.startswith("Y") and c[1:].isdigit()]

    # 3. Wide -> long: one row per country, item, element, unit, year
    long = df.melt(
        id_vars=["Area", "Item", "Element", "Unit"],
        value_vars=year_cols,
        var_name="Year",
        value_name="Value",
    )

    # 4. Clean up
    long["Year"] = long["Year"].str[1:].astype(int)
    long = long.dropna(subset=["Value"])
    long.columns = [c.lower() for c in long.columns]
    long = long.drop_duplicates()
    long = long.sort_values(["area", "item", "element", "year"])
    return long


if __name__ == "__main__":
    raw = ingest()
    clean = transform(raw)
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    clean.to_csv(CLEAN_FILE, index=False)
    print(f"Clean rows: {len(clean)}")
    print(clean.head())
    print(f"Saved to: {CLEAN_FILE}")