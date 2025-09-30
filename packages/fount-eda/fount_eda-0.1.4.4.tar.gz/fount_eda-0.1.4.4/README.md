# fount

**fount** is a lightweight, single-file Python module (`fount.py`) that acts as a unified facade over **pandas**, **NumPy**, and **scikit-learn** — with a robust, **read-only EDA** engine for transformer-style tabular and time-series datasets. It computes a **regression-only DNN suitability score (0–100)** and produces an inspectable report with schema, missingness, distributions, relationships, time-series diagnostics, and recommendations.

EDA-only: fount never mutates your data. No feature engineering, no reindexing, no train/val/test splits.

---

## Features

- **Unified facade**: Access pandas/NumPy/sklearn from a single namespace: `fount.DataFrame`, `fount.array`, `fount.train_test_split`, etc.
- **Read-only EDA**:
  - Works with single or multi-target _regression_ datasets
  - Numeric relevance via `mutual_info_regression` (fallback to Spearman |ρ|)
  - Categorical relevance via correlation ratio (η²)
  - Optional time-series diagnostics: inferred frequency, irregularity/missing timeline share, ADF (if available), autocorrelation & seasonality strength
  - Leakage hints (target-like names, |r|≥0.99 to target, identical columns)
- **Suitability score (0–100)** with a transparent, weighted breakdown across 13 components
- **Ergonomics**:
  - Type-ahead friendly: materializes public symbols for IDE autocomplete
  - Priority-based symbol resolution (default: pandas → numpy → sklearn)
  - Helpful “Did you mean…?” suggestions for mistyped attributes

---

## Installation

**Option A — Drop-in module (recommended)**

1. Copy `fount.py` into your project.
2. `import fount` anywhere you need it.

**Option B — Editable install (local package)**

```bash
# if you place fount.py inside a folder named 'fount' with an __init__.py
pip install -e .
```

### Dependencies

- **Required:** `numpy`
- **Needed for EDA:** `pandas`
- **Nice to have (optional, auto-detected):**
  - `scikit-learn` (for `mutual_info_regression` and re-exports)
  - `scipy` (for skew/kurtosis; otherwise returns `None`)
  - `statsmodels` (for ADF test; otherwise skipped)

> fount gracefully degrades when optional deps are missing (falls back or omits those metrics).

---

## Quick Start

```python
import fount

# pandas via fount
df = fount.read_csv("data.csv")
df2 = fount.DataFrame({"a": [1, 2, 3]})
merged = fount.merge(df, df2, how="left")

# numpy via fount
arr = fount.np.array([1, 2, 3, 4])      # or fount.array(...) if you prefer
print(fount.np.mean(arr))               # or set numpy priority first (see below)

# scikit-learn via fount
X_tr, X_te, y_tr, y_te = fount.train_test_split(X, y, test_size=0.2, random_state=42)
rf = fount.ensemble.RandomForestRegressor(n_estimators=300, random_state=0).fit(X_tr, y_tr)
print(rf.score(X_te, y_te))

# regression-only EDA + DNN suitability (0–100) for tabular/time-series
rep = fount.eda(df, target="Units", datetime_col="date")  # datetime_col optional
print("Suitability:", rep.suitability_score)

# pretty print to stdout
fount.eda_print(df, target="Units", datetime_col="date")

# markdown string (for docs/wikis)
md = fount.eda_md(df, target="Units", datetime_col="date")
```

---

## EDA & Scoring — What You Get

- **Schema**: row/column counts, feature:row ratio, dtype counts, constant & duplicate columns
- **Missingness**: total share, rows-with-any-missing, per-column missing %
- **Distributions**: per-numeric min/median/max/std/skew/kurtosis; overall outlier share (IQR rule); scale spread ratio
- **Relationships**:
  - Numeric↔target relevance: `mutual_info_regression` (if available) else Spearman |ρ| (per target)
  - Categorical↔target relevance: correlation ratio η² (per target)
  - Numeric↔numeric correlation matrix (proportion with |r|≥0.95)
- **Time Series (read-only)**:
  - Inferred frequency, irregular and missing timeline shares, unique periods, “enough history?”
  - Per-target: ADF p-value (if `statsmodels` available), autocorr at canonical lags, seasonality strength
- **Leakage hints**: Target-like column names, identical columns, or |r|≥0.99 with target
- **Recommendations**: Actionable suggestions (imputation, scaling, feature pruning, etc.)
- **Suitability score (0–100)** with breakdown across 13 components

### Score Components & Weights

| Component               | Weight |
| ----------------------- | :----: |
| size_adequacy           |   15   |
| feature_to_row_ratio    |   10   |
| missingness             |   10   |
| categorical_cardinality |   8    |
| target_quality          |   8    |
| multicollinearity       |   8    |
| scale_heterogeneity     |   5    |
| outliers                |   5    |
| ts_quality              |   10   |
| leakage_risk            |   6    |
| redundancy              |   5    |
| split_viability         |   5    |
| meta_completeness       |   5    |

> The final score is the weighted sum (0–1) × 100. For multi-target, fount computes per-target scores and an overall average.

---

## API Overview

### Top-Level EDA

```python
rep = fount.eda(df, target="Units", datetime_col=None, freq=None,
                max_mi_features=60, max_cat_features=80, corr_method="spearman")
```

- `eda(...)` → `EdaReport`
- `eda_report_and_score(...)` → `EdaReport` (same as `eda`, explicit name)
- `eda_md(...)` → markdown `str`
- `eda_print(...)` → prints markdown to stdout

**`EdaReport` fields**

```python
rep.schema                 # dict (counts, dtypes, constants, duplicates, targets)
rep.missingness            # dict (overall, per-row, per-column)
rep.distributions          # dict (numeric summary, outlier share, scale spread)
rep.relationships          # dict (corr stats, MI/Spearman, cat η²)
rep.time_series            # dict (inferred freq, irregular/missing shares, ADF, AC, seasonality)
rep.target                 # dict (per-target skew/kurtosis/zero share)
rep.score_breakdown        # EdaScoreBreakdown (0–1 per component)
rep.suitability_score      # float (0–100)
rep.recommendations        # list[str]
rep.suitability_score_by_target        # Optional[dict]
rep.score_breakdown_by_target          # Optional[dict]
rep.to_dict()              # serialize to dict
rep.to_markdown()          # markdown string
```

**`EdaScoreBreakdown`**

- 13 components (0–1). `weighted_total()` returns the weighted 0–1 sum.

### Facade & Backends

- `fount.pd`, `fount.np`, `fount.sk` — namespaced backend proxies
- Common NumPy constructors exposed at top level: `fount.array`, `fount.arange`, `fount.mean`, ...
- sklearn conveniences re-exported at top level:
  - `fount.train_test_split`
  - `fount.OneHotEncoder`, `fount.ColumnTransformer`, `fount.Pipeline`
  - `fount.RandomForestRegressor` (and access to full `fount.ensemble.*`)

**Priority control**

```python
# default priority: pandas -> numpy -> sklearn
fount.set_priority(["numpy", "pandas", "sklearn"])  # prefer numpy symbols first
```

**Autocomplete boost**

- fount materializes public symbols from installed backends into the module namespace (without shadowing Python built-ins).

---

## Usage Patterns & Tips

**Top features by relevance (numeric)**

```python
rep = fount.eda(df, target="Units")
mi = rep.relationships.get("mutual_information_top_by_target", {})
top = next(iter(mi.values()), {})  # first target's MI dict
print(sorted(top.items(), key=lambda kv: kv[1], reverse=True)[:10])
```

**Top categorical features (η²)**

```python
crt = rep.relationships.get("cat_corr_ratio_top_by_target", {})
top_cat = next(iter(crt.values()), {})
print(sorted(top_cat.items(), key=lambda kv: kv[1], reverse=True)[:10])
```

**Time-series diagnostics only**

```python
rep = fount.eda(df, target="Units", datetime_col="date")
print(rep.time_series)
```

**Markdown report to a file**

```python
with open("EDA_Report.md", "w") as f:
    f.write(fount.eda_md(df, target="Units", datetime_col="date"))
```

---

## Limitations

- **Regression only.** Classification metrics/diagnostics are not implemented.
- **Read-only.** No data mutation, imputation, encoding, scaling, resampling, or feature engineering.
- **MI sampling.** If rows > 8,000, mutual information is computed on a sample of 8k rows for speed.
- **Optional deps.** ADF requires `statsmodels`; skew/kurtosis require `scipy`. Without them, those metrics are omitted/gracefully degraded.

---

## 🔧 Design Notes

- **No hidden state**: EDA results are deterministic given inputs and installed backends.
- **Safety**: Python built-ins are protected from symbol shadowing.
- **Graceful degradation**: Missing optional deps do not raise; features are skipped or replaced with fallbacks.

---

## FAQ

**Q: What’s the difference between `eda`, `eda_md`, and `eda_print`?**

- `eda` returns a structured `EdaReport`.
- `eda_md` returns a markdown summary string.
- `eda_print` prints that markdown to stdout.

**Q: Can I use fount without scikit-learn / statsmodels / scipy?**  
Yes. You’ll still get schema/missingness/distributions/correlations. MI falls back to Spearman; ADF and skew/kurtosis are omitted if their libs are missing.

**Q: Does fount change my DataFrame?**  
No. EDA-only. It never mutates your data.

**Q: How do I prefer NumPy symbols over pandas?**  
Call `fount.set_priority(["numpy", "pandas", "sklearn"])`.

---

## Roadmap (ideas)

- Optional classification diagnostics
- Pluggable scoring weights
- Export helpers (HTML/JSON report writer)

---

## License

## MIT License

## Acknowledgments

Built to streamline EDA for transformer-style tabular/time-series workflows while keeping a simple, single-file footprint.
