import os
import pandas as pd
import geopandas as gpd
import folium
from sqlalchemy import create_engine
from dotenv import load_dotenv

# ENV laden
load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DB = os.getenv("MYSQL_DB")

TABLE_NAME = "hotels"

# MySQL Connection
engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

def main():
    # Daten aus MySQL laden
    query = f"""
    SELECT
        hotel_name,
        city_code,
        price,
        rating,
        latitude,
        longitude
    FROM {TABLE_NAME}
    WHERE latitude IS NOT NULL AND longitude IS NOT NULL
    """
    df = pd.read_sql(query, engine)

    print(f"Loaded {len(df)} rows from MySQL")

    # GeoDataFrame
    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df.longitude, df.latitude),
        crs="EPSG:4326"
    )

    # Karte zentrieren (Schweiz)
    m = folium.Map(location=[46.8, 8.3], zoom_start=7)

    for _, row in gdf.iterrows():
        folium.CircleMarker(
            location=[row.latitude, row.longitude],
            radius=4,
            popup=f"{row.hotel_name}<br>Price: {row.price}<br>Rating: {row.rating}",
            color="blue",
            fill=True,
            fill_opacity=0.6
        ).add_to(m)

    # Karte speichern
    os.makedirs("reports", exist_ok=True)
    m.save("reports/hotel_map.html")
    print("Map saved to reports/hotel_map.html")

if __name__ == "__main__":
    main()
