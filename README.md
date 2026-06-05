# 🛒 Retail Sales Predictive Analytics Pipeline

A machine learning regression pipeline that predicts retail transaction revenue across a 50K-record multi-channel dataset. Built as a business analytics data product for **sales forecasting**, **regional demand planning**, **CLV estimation**, and **behavioral segmentation** — with direct applications to fintech and growth analytics contexts.

---

## 🏆 Key Results

| Model | R² | RMSE | Notes |
|---|---|---|---|
| **Random Forest** | **0.9999** | **$9.45** | Best model — near-perfect accuracy |
| XGBoost | ~0.999 | — | Second best |
| Linear Regression | 0.8595 | $316.38 | Strong baseline |
| Ridge / Lasso | — | — | Regularized linear benchmarks |

> **5 models benchmarked total.** Random Forest achieves production-grade accuracy with RMSE under $10 on transaction values averaging ~$1,004.

---

## 🔑 Feature Importance

Top predictors (Random Forest):
1. **`Quantity`** — dominant driver of transaction value
2. **`Unit_Price`** — price per unit directly determines revenue
3. **`Discount`** — significant leverage on final transaction amount
4. Demographic & temporal features (Age, Region, Month) contribute modestly

---

## 🗂️ Project Structure

```
retail-sales-ml/
├── retail_EDA.ipynb              # Exploratory data analysis, time series, visualizations
├── engineering.ipynb             # Feature engineering: encoding, age binning, temporal features
├── modeling.ipynb                # Model training & evaluation: 5 regression models
├── engUtl.py                     # Encoding utility functions (target, label, one-hot)
├── data/
│   └── retail_data_synthetic_50k.xlsx   # Raw dataset (50K transactions, 13 columns)
├── requirements.txt              # Python dependencies
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3** | Core language |
| **Pandas / NumPy** | Data manipulation and numerical computation |
| **Scikit-learn** | Model training, preprocessing, evaluation metrics |
| **XGBoost** | Gradient-boosted regression |
| **Matplotlib / Seaborn** | Visualization and EDA plots |
| **Statsmodels** | Time series decomposition (STL, seasonal decompose) |
| **Jupyter Notebook** | Interactive development environment |
| **openpyxl** | Excel file I/O |

---

## 💼 Business Use Case

This pipeline is designed to support data-driven decisions across a multi-channel retail operation:

| Business Problem | ML Solution |
|---|---|
| **Sales Forecasting** | Predict `Total_Amount` by region, category, and channel with <$10 RMSE |
| **Regional Demand Planning** | Region-level revenue predictions inform inventory allocation and logistics |
| **Customer Lifetime Value (CLV)** | Aggregate per-customer predicted revenue to estimate long-term value |
| **Behavioral Segmentation** | Cluster customers by feature patterns (Online/In-store, payment type, age group) |
| **Pricing Optimization** | Quantify `Unit_Price` and `Discount` elasticity to optimize promotional strategy |

The dataset spans 4 years (2020–2023), 4 geographic regions (North, South, East, West), 5 product categories, 3 payment methods, and online/in-store channels — enabling granular multi-dimensional analysis.

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd retail-sales-ml
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run notebooks in order

```bash
jupyter notebook
```

Execute in this sequence:

| Step | Notebook | Output |
|---|---|---|
| 1 | `retail_EDA.ipynb` | EDA insights, visualizations |
| 2 | `engineering.ipynb` | `data/eng_data.csv` |
| 3 | `modeling.ipynb` | Model metrics, feature importances |

> **Note:** `engineering.ipynb` must be run before `modeling.ipynb` to generate `data/eng_data.csv`.

---

## 📊 Dataset

| Property | Value |
|---|---|
| Records | 50,000 transactions |
| Columns | 13 (12 features + 1 target) |
| Date range | January 2020 – December 2023 |
| Target variable | `Total_Amount` (range: $3.48 – $4,477.14, mean: ~$1,004) |
| Unique customers | ~2,000 |

**Columns:** `Transaction_ID`, `Customer_ID`, `Gender`, `Age`, `Category`, `Quantity`, `Unit_Price`, `Discount`, `Date`, `Store_Region`, `Online_Or_Offline`, `Payment_Method`, `Total_Amount`

---

## 📝 Notes

- Data cleaning validates arithmetic consistency of `Total_Amount` (found 0 arithmetic errors after tolerance check)
- Feature engineering produces ~30 features via one-hot encoding and temporal decomposition
- All models use an 80/20 train/test split with `random_state=42` for reproducibility
