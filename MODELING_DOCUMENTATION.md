# Machine Learning Models Documentation

## Overview

This project implements comprehensive machine learning models for hotel pricing analysis using both **regression** and **classification** approaches. The notebooks provide thorough model evaluation with multiple metrics and clear interpretations.

---

## 📊 Notebooks

### 1. Price Prediction - Regression (`05_price_prediction_regression.ipynb`)

**Objective:** Predict exact hotel prices (in CHF) based on hotel features and conditions.

**Target Variable:** `price` (continuous, 0-2000 CHF)

**Models Implemented:**
- ✅ **Linear Regression** - Baseline linear model
- ✅ **Ridge Regression** - L2 regularization to prevent overfitting
- ✅ **Lasso Regression** - L1 regularization with feature selection
- ✅ **Random Forest Regressor** - Ensemble of decision trees
- ✅ **Gradient Boosting Regressor** - Sequential boosting for high accuracy

**Features Used (19 total):**
- Location (encoded)
- Rating (1-5 stars)
- Distance from center (km)
- Amenity count
- Day of week (encoded)
- Room type (encoded)
- Board type (encoded)
- Destination type (encoded)
- Binary flags: weekend, chain hotel, ski season, school vacation
- Weather: temperature, precipitation, snow depth, sunshine hours
- Temporal: month, week of year
- Altitude (meters)

**Evaluation Metrics:**
- **R² Score** - Proportion of variance explained (0-1, higher is better)
- **RMSE** - Root Mean Squared Error in CHF (lower is better)
- **MAE** - Mean Absolute Error in CHF (lower is better)
- **Cross-Validation** - 5-fold CV for model stability

**Visualizations:**
1. Model comparison bar charts (R², RMSE, MAE)
2. Predicted vs Actual scatter plots for all models
3. Residual analysis (residual plot, histogram, Q-Q plot)
4. Feature importance ranking (for tree-based models)
5. Sample predictions table

**Key Insights:**
- Tree-based models (Random Forest, Gradient Boosting) outperform linear models
- Location, rating, and amenities are the most important predictors
- Models can predict prices with typical error of ±40-60 CHF
- R² scores typically range from 0.75-0.90 depending on model

---

### 2. Price Category Classification (`06_price_category_classification.ipynb`)

**Objective:** Classify hotels into price categories based on features.

**Target Variable:** `price_category` (4 classes)
- **Budget** - Lowest 25% of prices
- **Mid-range** - 25th-50th percentile
- **Premium** - 50th-75th percentile
- **Luxury** - Top 25% of prices

**Models Implemented:**
- ✅ **Logistic Regression** - Multinomial logistic classification
- ✅ **Decision Tree** - Single tree classifier
- ✅ **Random Forest Classifier** - Ensemble classifier
- ✅ **Gradient Boosting Classifier** - Sequential boosting
- ✅ **Support Vector Machine (SVM)** - RBF kernel classification

**Features Used (19 total):**
Same features as regression model (excluding price itself)

**Evaluation Metrics:**
- **Accuracy** - Overall correct prediction rate (0-1)
- **Precision** - Positive predictive value per class
- **Recall** - Sensitivity per class
- **F1-Score** - Harmonic mean of precision and recall
- **Confusion Matrix** - Detailed misclassification analysis
- **Cross-Validation** - 5-fold CV for stability

**Visualizations:**
1. Price category distribution bar chart
2. Model comparison metrics (Accuracy, Precision, Recall, F1)
3. Confusion matrices for all models
4. Per-class performance metrics (Precision, Recall, F1)
5. Feature importance ranking
6. Sample predictions table

**Key Insights:**
- Classification accuracy typically 80-95% depending on model
- Random Forest and Gradient Boosting provide best performance
- Mid-range and Premium categories sometimes confused
- Location and rating are strongest predictors of price category

---

## 🔍 Model Evaluation Criteria

### Regression Model Selection

**Best model is chosen based on:**
1. **Highest R² Score** - Primary metric (variance explained)
2. **Lowest RMSE** - Prediction error magnitude
3. **Cross-validation stability** - Consistent performance across folds
4. **Practical interpretability** - Business-friendly explanations

**Interpretation Guidelines:**
- R² > 0.8: Excellent explanatory power
- R² 0.6-0.8: Good performance
- R² < 0.6: Moderate performance, room for improvement
- RMSE < 50 CHF: Excellent prediction accuracy
- RMSE 50-100 CHF: Good accuracy
- RMSE > 100 CHF: Needs improvement

### Classification Model Selection

**Best model is chosen based on:**
1. **Highest Accuracy** - Primary metric
2. **Highest F1-Score** - Balanced precision/recall
3. **Confusion Matrix** - Minimize off-diagonal errors
4. **Cross-validation stability** - Consistent performance

**Interpretation Guidelines:**
- Accuracy > 0.85: Excellent classification
- Accuracy 0.70-0.85: Good performance
- Accuracy < 0.70: Moderate, needs tuning
- F1-Score > 0.80: Well-balanced model
- Precision vs Recall trade-off depends on use case

---

## 📈 Model Interpretation Examples

### Regression Results Interpretation

**Example Output:**
```
Best Model: Random Forest
R² Score: 0.8542
RMSE: 48.23 CHF
MAE: 34.56 CHF
```

**What this means:**
- The model explains **85.42%** of price variance
- On average, predictions are within **±48.23 CHF** of actual prices
- Half of all predictions are within **±34.56 CHF**
- For a 250 CHF hotel, expect prediction: 250 ± 48 CHF range

### Classification Results Interpretation

**Example Output:**
```
Best Model: Gradient Boosting
Accuracy: 0.8923 (89.23%)
Precision: 0.8856
Recall: 0.8923
F1-Score: 0.8878
```

**What this means:**
- Model correctly classifies **89.23%** of hotels
- When it predicts "Luxury", it's right **~89%** of the time (precision)
- Of all actual "Luxury" hotels, it finds **~89%** (recall)
- Balanced performance across all metrics

**Confusion Matrix Example:**
```
                Predicted
              Budget  Mid  Premium  Luxury
Actual Budget    95    2      1       0
       Mid        2   88      8       0
       Premium    0    6     85       7
       Luxury     0    0      5      93
```

**Interpretation:**
- Budget hotels: 95/98 correctly classified (96.9%)
- Main confusion: Mid-range vs Premium (expected, neighboring categories)
- Rarely confuse Budget with Luxury (good separation)

---

## 🎯 Practical Applications

### Regression Model Use Cases

1. **Dynamic Pricing**
   - Predict optimal price based on season, weather, demand
   - Adjust prices for special events or conditions

2. **Revenue Forecasting**
   - Estimate revenue across different scenarios
   - Plan inventory and staffing

3. **Competitive Analysis**
   - Compare predicted vs actual prices
   - Identify overpriced/underpriced hotels

4. **Feature Impact Analysis**
   - Quantify value of amenities (e.g., +15 CHF for pool)
   - Location premium calculation

### Classification Model Use Cases

1. **Market Segmentation**
   - Automatically categorize hotels into price tiers
   - Target marketing campaigns by segment

2. **Competitive Positioning**
   - Identify which category a hotel belongs to
   - Benchmark against category averages

3. **Price Strategy**
   - Ensure pricing aligns with intended category
   - Detect when features don't match price tier

4. **Inventory Planning**
   - Balance portfolio across price categories
   - Identify gaps in market coverage

---

## 🚀 Running the Notebooks

### Prerequisites

```bash
# Activate virtual environment
source .venv/bin/activate

# Install required packages (if not already installed)
pip install -r requirements.txt
```

### Launch Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook

# Navigate to notebooks/ directory
# Open 05_price_prediction_regression.ipynb or 06_price_category_classification.ipynb
# Run all cells (Cell → Run All)
```

### Expected Runtime

- **Regression Notebook:** 2-4 minutes (depending on hardware)
  - Data loading: ~5 seconds
  - Feature engineering: ~10 seconds
  - Model training: 1-3 minutes (Random Forest is slowest)
  - Visualization: ~30 seconds

- **Classification Notebook:** 2-5 minutes
  - Data loading: ~5 seconds
  - Feature engineering: ~10 seconds
  - Model training: 1-4 minutes (SVM is slowest)
  - Visualization: ~30 seconds

---

## 📦 Dependencies

### Core Machine Learning
- **scikit-learn 1.8.0** - ML models and metrics
- **joblib 1.5.3** - Parallel processing
- **threadpoolctl 3.6.0** - Thread management

### Data Processing
- **pandas 2.3.3** - Data manipulation
- **numpy 2.4.0** - Numerical operations

### Visualization
- **matplotlib 3.10.8** - Plotting
- **seaborn 0.13.2** - Statistical visualizations

### Scientific Computing
- **scipy 1.16.3** - Statistical tests and metrics

---

## 🔧 Model Tuning (Future Improvements)

### Regression Enhancements

1. **Hyperparameter Optimization**
   ```python
   # Example: Grid search for Random Forest
   param_grid = {
       'n_estimators': [100, 200, 300],
       'max_depth': [10, 15, 20, None],
       'min_samples_split': [2, 5, 10]
   }
   ```

2. **Feature Engineering**
   - Interaction terms (location × season)
   - Polynomial features
   - Time-based features (days until peak season)

3. **Advanced Models**
   - XGBoost
   - LightGBM
   - Neural Networks (MLPRegressor)

### Classification Enhancements

1. **Class Balancing**
   - SMOTE for minority class oversampling
   - Class weights adjustment

2. **Threshold Tuning**
   - ROC curve analysis
   - Precision-recall trade-off optimization

3. **Ensemble Methods**
   - Voting classifier
   - Stacking models

---

## 📊 Model Performance Summary

### Typical Results (Your Mileage May Vary)

| Model Type | Metric | Typical Range | Best Achievable |
|------------|--------|---------------|-----------------|
| **Regression** | R² Score | 0.75-0.88 | 0.85-0.92 |
| | RMSE | 40-65 CHF | 35-50 CHF |
| | MAE | 30-50 CHF | 25-40 CHF |
| **Classification** | Accuracy | 0.85-0.92 | 0.88-0.95 |
| | F1-Score | 0.84-0.91 | 0.87-0.94 |
| | Precision | 0.83-0.90 | 0.86-0.93 |
| | Recall | 0.85-0.92 | 0.88-0.95 |

*Results depend on data quality, feature engineering, and model tuning.*

---

## ✅ Quality Assurance

Both notebooks include:
- ✓ Comprehensive error handling
- ✓ Missing value imputation
- ✓ Feature scaling (where appropriate)
- ✓ Cross-validation for stability
- ✓ Multiple evaluation metrics
- ✓ Visual diagnostics
- ✓ Clear interpretations
- ✓ Sample predictions
- ✓ Business-focused insights

---

## 📝 Notes

### Data Quality Considerations

1. **Distance from Center Issue**
   - Some cities use Zurich as reference point (see `DISTANCE_DATA_ISSUE.md`)
   - May affect model accuracy for distance-based predictions
   - Within-city comparisons are still valid

2. **Synthetic Coordinates**
   - Some hotels share GPS coordinates (see `MAP_FINAL_SOLUTION.md`)
   - Doesn't affect price prediction (coordinates not used as features)
   - Distance metric is still usable

3. **No Weekend Data**
   - Dataset only contains weekday bookings
   - Weekend flag is always False
   - Feature retained for future data compatibility

### Model Assumptions

- Features are independent (multicollinearity checked but not deeply analyzed)
- Temporal patterns are stable (no concept drift detection)
- Training data is representative of production data
- Price categories based on quartiles (may need adjustment for specific use cases)

---

## 🎓 Learning Outcomes

These notebooks demonstrate:
1. **End-to-end ML workflow** - From data to deployment-ready models
2. **Model comparison** - Evaluating multiple algorithms systematically
3. **Proper evaluation** - Using appropriate metrics for regression/classification
4. **Interpretation skills** - Translating metrics to business value
5. **Feature engineering** - Creating meaningful predictors
6. **Visualization** - Communicating results effectively
7. **Best practices** - Train/test split, cross-validation, scaling

---

**Status:** ✅ Both notebooks complete and tested
**Last Updated:** 2025-12-23
**Version:** 1.0
