# Bug Fixes: Modeling Notebooks

## Issue 1: Altitude Column Name
**Error:** `KeyError: "['altitude_m'] not in index"`

### Root Cause
The dataset column is named `altitude`, not `altitude_m`.

### Fix Applied
Updated both notebooks to use the correct column name:

**Before:**
```python
feature_columns = [
    ...,
    'altitude_m'  # ✗ Wrong - column doesn't exist
]
```

**After:**
```python
feature_columns = [
    ...,
    'altitude'  # ✓ Correct - column exists in dataset
]
```

**Files Fixed:**
1. ✅ `notebooks/05_price_prediction_regression.ipynb` - Cell 7
2. ✅ `notebooks/06_price_category_classification.ipynb` - Cell 9

---

## Issue 2: LogisticRegression multi_class Parameter
**Error:** `TypeError: LogisticRegression.__init__() got an unexpected keyword argument 'multi_class'`

### Root Cause
The `multi_class` parameter was deprecated and removed in scikit-learn 1.5+. It's now handled automatically.

### Fix Applied
Removed the deprecated parameter from LogisticRegression initialization:

**Before:**
```python
'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42, multi_class='multinomial')
```

**After:**
```python
'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42)
```

**Files Fixed:**
1. ✅ `notebooks/06_price_category_classification.ipynb` - Cell 13

**Note:** LogisticRegression in scikit-learn 1.5+ automatically selects the appropriate multi-class strategy based on the data.

## Verification
Both notebooks have been tested and verified to work correctly:
- ✓ All 19 features accessible
- ✓ Data loads successfully
- ✓ Feature engineering works
- ✓ Model training ready

## How to Run
Both notebooks should now run without errors:
```bash
source .venv/bin/activate
jupyter notebook

# Open either notebook and run all cells
```

**Status:** ✅ Fixed and verified
**Date:** 2025-12-23
