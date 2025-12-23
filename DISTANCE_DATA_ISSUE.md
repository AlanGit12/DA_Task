# Distance from Center - Data Quality Issue

## Problem in Notebook 03, Section 2

The scatter plot shows a strange bimodal distribution with distances either:
- **0-5 km** (city hotels)
- **90-160 km** (mountain/distant locations)

This looks wrong because it IS wrong.

## Root Cause

**The `distance_from_center` column measures distance from a CENTRAL REFERENCE POINT (Zurich), NOT from each city's own center.**

### Evidence

| City | Distance Range | What It Measures |
|------|---------------|------------------|
| **Zurich** | 0.3 - 1.2 km | ✓ From Zurich center (correct) |
| **Bern** | 0.1 km | ✗ From Zurich (30km away!) |
| **Geneva** | 0.5 - 2.4 km | ✗ From Zurich (280km away!) |
| **Basel** | 1.5 - 2.1 km | ✗ From Zurich (85km away!) |
| **Luzern** | 39-41 km | ✗ Actual distance Zurich→Luzern |
| **Arosa** | 107-108 km | ✗ Actual distance Zurich→Arosa |
| **Zermatt** | 161-163 km | ✗ Actual distance Zurich→Zermatt |
| **St. Moritz** | 138-139 km | ✗ Actual distance Zurich→St. Moritz |

## The Bimodal Pattern Explained

**Group 1: Cities with their OWN center coordinates (0-5 km)**
- Geneva, Basel, Bern measured from their own centers
- Shows realistic urban hotel distances

**Group 2: Cities using Zurich as reference (90-160 km)**  
- Arosa, Zermatt, St. Moritz, Interlaken, Chur
- Shows distance FROM ZURICH, not from city center
- Completely wrong for price-distance analysis

## Impact on Analysis

### ✗ **Sections 1-2: Overall Correlation (MISLEADING)**
- Mixes two different reference points
- Creates meaningless correlation
- Scatter plot is nonsensical
- **Should be ignored or used with heavy caveats**

### ✓ **Section 3: Per-Location Analysis (VALID)**
- Within each city, distances are relative to same reference
- Arosa hotels: all ~107km means "within Arosa" (1km variation)
- Geneva hotels: 0.5-2km means "within Geneva" 
- **This analysis IS meaningful** - shows if central vs peripheral hotels in SAME city have different prices

## What We Fixed

**Updated Notebook 03 to:**

1. **Section 1:** Added warning that overall correlation is problematic
2. **Section 2:** Replaced misleading scatter plot with:
   - Scatter plot WITH warning label
   - Histogram showing bimodal distribution
   - Clear explanation of the data issue
3. **Section 3:** Emphasized as "⭐ Meaningful Analysis"
4. **All sections:** Added explanatory notes about data quality

## Correct Interpretation

### Within-City Analysis (Valid)
- **Geneva:** Hotels 0.5-2km apart → price variation within Geneva
- **Arosa:** Hotels ~1km apart → price variation within Arosa
  - (All ~107km from reference, but 107.4-108.4 = 1km spread)

### Cross-City Analysis (Invalid)
- ✗ Comparing Geneva hotel (2km) with Arosa hotel (107km)
- ✗ This compares Geneva-center with Zurich-Arosa distance
- ✗ Meaningless correlation

## Recommendations

1. **Use Section 3** for analysis (per-location correlation)
2. **Interpret carefully:** Within-city distance variation only
3. **Ignore Sections 1-2** or treat as exploratory only
4. **Future improvement:** Recalculate distances from each city's actual center

## Data Quality Summary

This is the **third major data quality issue** in this dataset:

1. ✗ **Coordinates:** Duplicate lat/long across cities
2. ✗ **Distance:** Mixed reference points (some cities, some from Zurich)
3. ✗ **Synthetic data:** Same hotels in multiple cities with same coordinates

**Conclusion:** This appears to be **synthetic/test data**, not real hotel data.

---

**Status:** ✅ Issue documented and notebook updated with warnings  
**Valid Analysis:** Per-location correlation (Section 3) only  
**Invalid Analysis:** Overall correlation (Sections 1-2)
