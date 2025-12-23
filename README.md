# Diabetes Readmission Prediction - ML Models

Machine learning project for predicting hospital readmission in diabetes patients using ensemble learning and clustering analysis.

## Project Overview

Analysis of the Diabetes 130-US Hospitals dataset (1999-2008) with 101,766 patient records to predict readmission within 30 days of discharge.

**Target Classes:**
- NO - No readmission (53.9%)
- >30 - Readmitted after 30 days (34.9%)
- <30 - Readmitted within 30 days (11.2%)



## Dataset

- **Source:** 130 US Hospitals (1999-2008)
- **Records:** 101,766 patient encounters
- **Features:** 50+ (demographics, medical history, lab results, medications)
- **Split:** 80% train (81,413) / 20% test (20,354)

## Models & Results

### Classification Models

**Bagging Classifier (Random Forest)**
```
Accuracy: 68.68%
Precision: 0.67 (NO), 0.59 (>30), 1.00 (<30)
Recall:    0.84 (NO), 0.35 (>30), 1.00 (<30)
F1-Score:  0.74 (NO), 0.44 (>30), 1.00 (<30)
```

**Gradient Boosting Classifier** ⭐
```
Accuracy: 69.82%
Precision: 0.67 (NO), 0.62 (>30), 1.00 (<30)
Recall:    0.87 (NO), 0.34 (>30), 1.00 (<30)
F1-Score:  0.76 (NO), 0.44 (>30), 1.00 (<30)
```

### Clustering Analysis

- **K-Means Clustering:** 3 clusters with PCA visualization
- **Hierarchical Clustering:** Agglomerative with Ward linkage


## Usage

### 1. Data Preprocessing & Classification


**Steps:**
- Load and clean data
- Feature engineering
- Train Bagging and Boosting models
- Evaluate performance
- Generate confusion matrices

### 2. Clustering Analysis

```bash
jupyter notebook data_clustering.ipynb
```

**Steps:**
- Apply K-Means clustering
- Perform Hierarchical clustering
- Visualize clusters with PCA
- Generate dendrograms

## Key Findings

- **Best Model:** Gradient Boosting (69.82% accuracy)
- **Perfect Performance:** Both models achieve 100% metrics for <30 days class
- **Challenge:** >30 days class most difficult to predict (F1: 0.44)
- **Clustering:** Reveals distinct patient groups for targeted interventions

## Technologies Used

- Python 3.x
- pandas, numpy - Data manipulation
- scikit-learn - ML models
- matplotlib, seaborn - Visualization
- plotly - Interactive plots

## Future Improvements

- [ ] Deep learning models (LSTM, CNN)
- [ ] SMOTE for class imbalance
- [ ] Feature importance analysis
- [ ] Cross-validation optimization
- [ ] Real-time prediction API

## Dashboard

Interactive dashboard available at: [https://diabetes-readmission.streamlit.app/]

## License

MIT License

## Contact

amirthaganeshramesh@gmail.com
AMIRTHA GANESH R

---

**Note:** `diabetic_data.csv` not included due to size. Download from [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008)
