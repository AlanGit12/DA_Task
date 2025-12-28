from sqlalchemy import create_engine, text
import pandas as pd
import os
from dotenv import load_dotenv

# ENV laden
load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DB = os.getenv("MYSQL_DB")

engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

def main():
    query = text("""
        SELECT
            city_code,
            COUNT(*) AS n_hotels,
            ROUND(AVG(price), 2) AS avg_price,
            ROUND(AVG(rating), 2) AS avg_rating
        FROM hotels
        GROUP BY city_code
        ORDER BY avg_price DESC
        LIMIT 10;
    """)

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)

    print("\nTop 10 cities by average hotel price:\n")
    print(df)

if __name__ == "__main__":
    main()