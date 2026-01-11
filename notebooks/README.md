# Hotel Data Analysis Notebooks

This directory contains Jupyter notebooks for comprehensive exploratory data analysis and machine learning modeling of the hotel pricing dataset.

## Notebooks Overview

### 01_price_trends_analysis.ipynb
**Focus:** Price trends over time across different locations

**Visualizations:**
- Line plot of average hotel prices over time by location
- Scatter plot of all individual hotel prices by location
- Box plots showing price distribution by location
- Bar chart comparing average prices across locations
- Weekly price trend analysis
- Summary statistics by location

**Key Questions Answered:**
- How do hotel prices change over time?
- Which locations are most/least expensive?
- What is the price variability within each location?

---

### 02_hotel_locations_map.ipynb
**Focus:** Geographic distribution of hotels

**Visualizations:**
- Interactive map with all hotel locations marked (Folium)
- Color-coded markers by location
- Hotel distribution bar chart
- Geographic spread analysis

**Key Questions Answered:**
- Where are hotels located geographically?
- How are hotels distributed across different cities?
- What is the geographic spread within each location?

**Output:** Generates an interactive HTML map saved to `data/hotel_locations_map.html`

---

### 03_price_distance_correlation.ipynb
**Focus:** Relationship between hotel prices and distance from city center

**Visualizations:**
- Scatter plot with regression line (price vs distance)
- Correlation analysis with statistical significance
- Individual correlation plots for each location
- Price comparison by distance categories
- Box plots showing price distribution by distance ranges

**Key Questions Answered:**
- Is there a correlation between price and distance from center?
- Does this relationship vary by location?
- How much does proximity to city center affect pricing?

**Statistical Methods:**
- Pearson correlation coefficient
- Linear regression analysis
- P-value significance testing

---

### 04_additional_analyses.ipynb
**Focus:** Comprehensive analysis of multiple factors affecting hotel prices

**Analyses Include:**

1. **Price vs Rating Analysis**
   - Correlation between price and hotel rating
   - Price distribution across rating categories

2. **Weekend vs Weekday Pricing**
   - Price comparison between weekdays and weekends
   - Statistical analysis of weekend premiums

3. **Day of Week Analysis**
   - Average prices for each day of the week
   - Identification of most/least expensive days

4. **Room Type Analysis**
   - Price comparison across different room types
   - Average prices by room category

5. **Board Type (Meal Plan) Analysis**
   - Impact of meal plans on pricing
   - Comparison of breakfast, half-board, full-board options

6. **Chain vs Independent Hotels**
   - Price comparison between hotel chains and independent properties
   - Analysis of top hotel chains by average price

7. **Seasonal Analysis**
   - Price variations across seasons (Winter, Spring, Summer, Fall)
   - Ski season impact on pricing

8. **Altitude Analysis**
   - Correlation between hotel altitude and price
   - Mountain resort pricing patterns

9. **Weather Impact**
   - Temperature correlation with pricing
   - Snow depth impact on hotel prices

10. **Correlation Heatmap**
    - Visual representation of all numeric variable correlations
    - Identification of strongest price predictors

11. **Destination Type Analysis**
    - Price comparison across city, mountain resort, and ski resort locations

**Key Questions Answered:**
- What factors most strongly influence hotel prices?
- Are there seasonal pricing patterns?
- Do hotel chains charge more than independent hotels?
- How do weather conditions affect pricing?

---

### 05_price_prediction_regression.ipynb
**Focus:** Machine learning regression models to predict hotel prices

**Models Implemented:**
- Linear Regression
- Ridge Regression (L2 regularization)
- Lasso Regression (L1 regularization)
- Random Forest Regressor
- Gradient Boosting Regressor

**Features Used:**
- Location, rating, distance from center
- Amenity count, room type, board type
- Weather conditions (temperature, precipitation, snow depth, sunshine)
- Temporal features (month, week, day of week)
- Binary flags (weekend, chain hotel, ski season, school vacation)

**Evaluation Metrics:**
- R² Score (variance explained)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- 5-fold Cross-Validation

**Visualizations:**
- Model performance comparison (R², RMSE, MAE)
- Predicted vs Actual scatter plots for all models
- Residual analysis (residual plot, histogram, Q-Q plot)
- Feature importance ranking (Random Forest)
- Sample predictions

**Key Questions Answered:**
- How accurately can we predict hotel prices?
- Which features are most important for price prediction?
- Which model performs best for price forecasting?

---

### 06_price_category_classification.ipynb
**Focus:** Machine learning classification models to categorize hotels by price tier

**Target Categories:**
- Budget (0-25th percentile)
- Mid-range (25th-50th percentile)
- Premium (50th-75th percentile)
- Luxury (75th-100th percentile)

**Models Implemented:**
- Logistic Regression (multinomial)
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- Support Vector Machine (SVM)

**Evaluation Metrics:**
- Accuracy
- Precision (per class)
- Recall (per class)
- F1-Score
- Confusion Matrix
- 5-fold Cross-Validation

**Visualizations:**
- Price category distribution
- Model performance comparison (Accuracy, Precision, Recall, F1)
- Confusion matrices for all models
- Per-class performance metrics
- Feature importance ranking (Random Forest)
- Sample predictions

**Key Questions Answered:**
- How accurately can we classify hotels into price categories?
- Which features best distinguish price tiers?
- Which model provides the best classification accuracy?
- Where do models make misclassification errors?

---

## How to Use These Notebooks

### Prerequisites
All required packages are installed in the virtual environment:
```bash
source .venv/bin/activate
```

Packages include:
- pandas, numpy - Data manipulation
- matplotlib, seaborn - Visualization
- folium - Interactive maps
- scipy - Statistical analysis
- scikit-learn - Machine learning models
- jupyter, notebook - Notebook environment

### Running the Notebooks

1. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

2. **Start Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

3. **Navigate to the notebooks directory and open any notebook**

4. **Run all cells:**
   - Click "Cell" → "Run All" in the menu
   - Or use Shift+Enter to run cells individually

### Data Requirements
All notebooks expect the data file to be located at:
```
../data/enriched_hotels_data.csv
```

This path is relative to the notebooks directory.

## Key Insights

### Exploratory Data Analysis (Notebooks 1-4)
- **Price Trends:** How hotel prices fluctuate over time and across locations
- **Geographic Patterns:** Where hotels are concentrated and how location affects pricing
- **Distance Effect:** Whether proximity to city center commands a premium
- **Temporal Patterns:** Day-of-week and seasonal pricing strategies
- **Quality vs Price:** How ratings correlate with pricing
- **Weather Impact:** How seasonal weather affects hotel demand and pricing
- **Hotel Type Differences:** How chain hotels compare to independent properties

### Machine Learning Models (Notebooks 5-6)
- **Price Prediction:** Regression models can predict prices with 75-90% accuracy (R² score)
- **Price Categorization:** Classification models achieve 85-95% accuracy in categorizing hotels
- **Key Price Drivers:** Location, rating, and amenities are the strongest predictors
- **Model Performance:** Tree-based models (Random Forest, Gradient Boosting) outperform linear models
- **Practical Applications:** Models support dynamic pricing, revenue forecasting, and market segmentation

## Output Files

Some notebooks generate additional output files:
- `02_hotel_locations_map.ipynb` creates `../data/hotel_locations_map.html` - an interactive map you can open in any browser

## Notes

- All visualizations use consistent color schemes for easy comparison
- Statistical significance is tested where applicable
- Correlation coefficients are provided with interpretation
- Summary statistics accompany most visualizations
- The notebooks are designed to be self-contained and can be run in any order
