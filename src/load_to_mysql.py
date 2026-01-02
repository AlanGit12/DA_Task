import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

def main():
    load_dotenv()

    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST", "127.0.0.1")
    port = os.getenv("MYSQL_PORT", "3306")
    db = os.getenv("MYSQL_DB")
    table = os.getenv("MYSQL_TABLE", "hotels")
    csv_path = os.getenv("CSV_PATH", "data/enriched_hotels_data.csv")

    if not all([user, password, db]):
        raise ValueError("MYSQL_USER / MYSQL_PASSWORD / MYSQL_DB fehlen in der .env")

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV nicht gefunden: {csv_path}")

    # Engine
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}")

    # Load CSV
    df = pd.read_csv(csv_path)

    # Write table
    df.to_sql(table, con=engine, if_exists="replace", index=False)

    # Quick checks
    with engine.connect() as conn:
        count = conn.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()
        print(f"Loaded {count} rows into `{db}`.`{table}`")
        cols = conn.execute(text(f"SHOW COLUMNS FROM {table}")).fetchall()
        print(f"Columns: {[c[0] for c in cols]}")

if __name__ == "__main__":
    main()