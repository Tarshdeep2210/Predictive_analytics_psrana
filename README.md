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
