from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "data" / "livestock.db"
SQL_FILE = BASE_DIR / "queries.sql"


def run_queries():
    conn = sqlite3.connect(DB_FILE)
    sql_text = SQL_FILE.read_text(encoding="utf-8")
    queries = [q.strip() for q in sql_text.split(";") if q.strip()]

    for i, query in enumerate(queries, start=1):
        print(f"--- Query {i} ---")
        print(pd.read_sql_query(query, conn).to_string(index=False))
        print()
    conn.close()


if __name__ == "__main__":
    run_queries()