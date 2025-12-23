# Quick Start Guide for EDA Notebooks

## Starting Jupyter Notebook

```bash
# 1. Activate virtual environment
source .venv/bin/activate

# 2. Start Jupyter Notebook
jupyter notebook

# 3. Your browser will open automatically
# Navigate to the 'notebooks' folder and open any .ipynb file
```

## Available Notebooks

1. **01_price_trends_analysis.ipynb** - Price trends over time by location
2. **02_hotel_locations_map.ipynb** - Interactive hotel location map
3. **03_price_distance_correlation.ipynb** - Price vs distance correlation
4. **04_additional_analyses.ipynb** - Comprehensive multi-factor analysis

## Running a Notebook

Once you open a notebook in Jupyter:
- Click "Cell" → "Run All" to execute all cells
- Or use `Shift + Enter` to run cells one by one

## Expected Outputs

- **Visualizations:** All charts and graphs will appear inline
- **Statistics:** Summary tables and correlation coefficients
- **Map File:** Notebook 02 creates `data/hotel_locations_map.html` that you can open in any browser

## Data Summary

Your dataset contains:
- **1,923 records**
- **13 locations** across Switzerland
- **Date range:** January 2026 to December 2026
- **37 data columns** including price, rating, location, weather, amenities, etc.

## Troubleshooting

If you get import errors:
```bash
source .venv/bin/activate
pip install matplotlib seaborn folium jupyter scipy
```

If Jupyter doesn't start:
```bash
pip install notebook
jupyter notebook
```
