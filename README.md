# Topsis-Tarshdeep-102316050

A Python package to implement the **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)** method for multi-criteria decision making.

## About TOPSIS

TOPSIS is a multi-criteria decision-making (MCDM) technique proposed by
Hwang and
Yoon (1981).

The core idea:

* The best alternative should have the **shortest distance from the ideal solution**
* And the **farthest distance from the negative-ideal solution**

## Mathematical Steps of TOPSIS

1. Normalize the decision matrix
2. Multiply by weights
3. Determine ideal best and ideal worst
4. Calculate separation measures
5. Calculate TOPSIS score
6. Rank alternatives based on score

## Installation

After uploading to PyPI:

```bash
pip install Topsis-Tarshdeep-102316050
```

## Usage (Command Line)

```bash
python -m topsis.topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

### Example:

```bash
python -m topsis.topsis data.csv "1,1,1,2" "+,+,-,+" output.csv
```

## Input File Format

* Must be a `.csv` file
* First column → Alternatives (non-numeric allowed)
* From 2nd to last columns → Numeric values only
* Must contain **at least 3 columns**

### Example:

```
Model,Price,Storage,Camera
M1,25000,128,12
M2,30000,256,16
M3,20000,128,8
```

## Output Format

Output file will contain:

* All original columns
* Topsis Score
* Rank (1 = Best)

## Error Handling

The program validates inputs before processing and handles errors appropriately.

* Checks correct number of command-line parameters
* Handles **File Not Found** exception
* Ensures input file has **at least 3 columns**
* Validates that columns from 2nd onward contain **numeric values only**
* Ensures number of **weights, impacts, and criteria are equal**
* Validates impacts must be only `'+'` or `'-'`
* Ensures weights and impacts are **comma-separated**

Appropriate error messages are displayed for invalid inputs.

## Package Naming Convention

Package name follows required format:

```
Topsis-Tarshdeep-102316050
```

## Testing the Package

After installation:

```bash
pip install Topsis-Tarshdeep-102316050
python -m topsis.topsis data.csv "1,1,1" "+,+,-" output.csv
```

## Assumptions

* Missing values are not allowed
* CSV file must be properly formatted
* All criteria are independent
* Ranking is based purely on mathematical TOPSIS score

## Author

Tarshdeep Kaur
Roll Number: 102316050

# Now What You Should Do

1. Paste this into your `README.md`
2. Commit and push
3. Build package:

```bash
python -m build
```

4. Upload to PyPI:

```bash
python -m twine upload dist/*
```
# Assignment 5 — Apply TOPSIS to Find Best Pre-trained Model (Text Summarization)

## Objective

To evaluate multiple **pre-trained text summarization models** on a common dataset and determine the best model using the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** multi-criteria decision-making method.

---

## Methodology

1. **Dataset Used:** XSum dataset (HuggingFace Datasets library).
2. Selected **12 random samples** from the test split.
3. Evaluated the following **5 models**:
   - google/pegasus-xsum
   - sshleifer/distilbart-xsum-12-6
   - t5-small
   - facebook/bart-base
   - sshleifer/distilbart-cnn-12-6
4. For each model we measured:
   - ROUGE-1 score (higher is better)
   - ROUGE-L score (higher is better)
   - Latency per sample in milliseconds (lower is better)
   - Number of parameters in millions (lower is better)
5. Applied TOPSIS:
   - Normalization of decision matrix
   - Weight assignment
   - Ideal best and worst calculation
   - Distance computation
   - Final TOPSIS score and ranking
6. Results saved to:topsis_summarization_xsum_small_results.csv
   
---

## TOPSIS Criteria Weights

| Criterion | Type | Weight |
|-----------|------|--------|
ROUGE-1 | Benefit | 0.40 |
ROUGE-L | Benefit | 0.30 |
Latency | Cost | 0.20 |
Parameters | Cost | 0.10 |

---

## Results Table (TOPSIS Ranking)

| Rank | Model | ROUGE-1 | ROUGE-L | Latency (ms/sample) | Params (M) | TOPSIS Score |
|------|-------|---------|---------|---------------------|------------|--------------|
| 1 | google/pegasus-xsum | 0.4679 | 0.3946 | 5594.59 | 766.57 | **0.6641** |
| 2 | sshleifer/distilbart-xsum-12-6 | 0.4343 | 0.3489 | 6968.65 | 408.45 | 0.6116 |
| 3 | t5-small | 0.1529 | 0.1120 | 941.14 | 60.51 | 0.3791 |
| 4 | facebook/bart-base | 0.1542 | 0.1102 | 1676.64 | 139.42 | 0.3490 |
| 5 | sshleifer/distilbart-cnn-12-6 | 0.1809 | 0.1339 | 3431.48 | 408.45 | 0.2725 |

---

## Best Model (TOPSIS Result)

**Model:** google/pegasus-xsum  
**TOPSIS Score:** 0.6641  
**ROUGE-1:** 0.4679  
**ROUGE-L:** 0.3946  
**Latency:** 5594.59 ms/sample  
**Parameters:** 766.57 Million  

### Conclusion

According to TOPSIS ranking considering both **quality metrics and efficiency**, **PEGASUS-XSum** is the best performing summarization model among the evaluated models.

---

# Assignment 6 — Data Generation using Modelling & Simulation + ML Comparison

## Objective

To generate a dataset using a **simulation model**, run **1000 simulations**, and compare multiple machine learning models to identify the best predictor.

---

## Simulation Model Used

**SIR Epidemic Model (Susceptible-Infected-Recovered)**  
Implemented using **SciPy ODE solver (solve_ivp)**.

### Governing Equations

- dS/dt = −βSI  
- dI/dt = βSI − γI  
- dR/dt = γI  

---

## Parameter Bounds

| Parameter | Lower | Upper |
|-----------|-------|-------|
β (infection rate) | 0.05 | 1.50 |
γ (recovery rate) | 0.05 | 1.00 |
I0 (initial infected) | 0.001 | 0.10 |
Days | 60 | 200 |

---

## Dataset Generation

- Total simulations: **1000**
- Runtime: **2.39 seconds**
- Output file:sir_simulation_dataset_1000.csv
- 
### Generated Features

Inputs:
- beta
- gamma
- I0
- days
- R0_basic = beta / gamma

Outputs:sir_simulation_dataset_1000.csv
- peak_I
- t_peak
- final_R

---

## Machine Learning Task

**Goal:** Predict `peak_I` using simulation parameters.

Train/Test split:
- 75% training
- 25% testing

---

## Models Compared (11 Models)

- Linear Regression
- Ridge
- Lasso
- ElasticNet
- KNN
- SVR
- Decision Tree
- Random Forest
- Extra Trees
- Gradient Boosting
- MLP Neural Network

Evaluation Metrics:
- R² Score (higher better)
- MAE (lower better)
- RMSE (lower better)
- Training Time

---

## Results Table

| Model | R² | MAE | RMSE | Train Time (s) |
|-------|-----|-----|------|----------------|
ExtraTrees | **0.999656** | 0.00244 | 0.00387 | 0.41 |
GradientBoosting | 0.999424 | 0.00331 | 0.00501 | 0.16 |
RandomForest | 0.999178 | 0.00372 | 0.00599 | 0.61 |
DecisionTree | 0.998558 | 0.00478 | 0.00793 | 0.0047 |
KNN | 0.981777 | 0.01847 | 0.02819 | 0.0061 |
MLP | 0.967690 | 0.02895 | 0.03754 | 0.096 |
SVR | 0.875321 | 0.06299 | 0.07374 | 0.0043 |
Lasso | 0.844114 | 0.05500 | 0.08245 | 0.0039 |
ElasticNet | 0.843705 | 0.05508 | 0.08256 | 0.0016 |
Ridge | 0.843339 | 0.05516 | 0.08266 | 0.0068 |
LinearRegression | 0.842861 | 0.05515 | 0.08279 | 0.0020 |

Saved file: model_comparison_table.csv

---

## Best Model (ML Comparison)

**Model:** ExtraTrees Regressor  

Metrics:
- R²: 0.999656
- MAE: 0.00244
- RMSE: 0.00387

### Conclusion

The **ExtraTrees ensemble model** achieved the highest predictive accuracy with minimal error, making it the best model for predicting epidemic peak infection from simulation parameters.

---

# Assignment 7 — Mashup Application (CLI + WebApp)

## Objective

Develop a mashup system that:

1. Downloads N YouTube videos of a singer
2. Converts videos to audio
3. Cuts first Y seconds
4. Merges all clips into one file

---

## Program 1 — CLI Python Script

File name:102316050.py

### Usage

```
python <RollNumber>.py "<SingerName>" <NumberOfVideos> <AudioDuration> <OutputFileName>
```

Example:

python 101556.py "Sharry Maan" 20 20 output.mp3

### Validations Implemented

- Correct number of arguments
- Number of videos > 10
- Audio duration > 20 seconds
- Proper error messages
