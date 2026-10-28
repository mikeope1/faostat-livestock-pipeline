from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
CLEAN_FILE = BASE_DIR / "data" / "clean" / "livestock_long.csv"
DB_FILE = BASE_DIR / "data" / "livestock.db"
TABLE = "livestock_production"


def load():
    if not CLEAN_FILE.exists():
        raise FileNotFoundError(f"Clean file not found: {CLEAN_FILE}. Run transform.py first.")

    df = pd.read_csv(CLEAN_FILE)

    conn = sqlite3.connect(DB_FILE)
    # "replace" rebuilds the table each run, so running this twice never creates duplicates
    df.to_sql(TABLE, conn, if_exists="replace", index=False)

    count = conn.execute(f"SELECT COUNT(*) FROM {TABLE}").fetchone()[0]
    print(f"Loaded {count} rows into table '{TABLE}'")
    print(f"Database file: {DB_FILE}")
    conn.close()


if __name__ == "__main__":
    load()