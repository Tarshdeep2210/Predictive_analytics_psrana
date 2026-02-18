import sys
import os
import pandas as pd
import numpy as np


def validate_input(args):
    if len(args) != 5:
        print("Error: Incorrect number of parameters.")
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        sys.exit(1)

    input_file = args[1]
    weights = args[2]
    impacts = args[3]
    output_file = args[4]

    # File exists check
    if not os.path.isfile(input_file):
        print("Error: Input file not found.")
        sys.exit(1)

    return input_file, weights, impacts, output_file


def validate_dataframe(df, weights, impacts):
    if df.shape[1] < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)

    # Check numeric columns (2nd to last)
    try:
        df.iloc[:, 1:] = df.iloc[:, 1:].astype(float)
    except ValueError:
        print("Error: From 2nd to last columns must contain numeric values only.")
        sys.exit(1)

    num_cols = df.shape[1] - 1

    weights_list = weights.split(',')
    impacts_list = impacts.split(',')

    if len(weights_list) != num_cols or len(impacts_list) != num_cols:
        print("Error: Number of weights, impacts and numeric columns must be the same.")
        sys.exit(1)

    # Validate impacts
    for impact in impacts_list:
        if impact not in ['+', '-']:
            print("Error: Impacts must be either '+' or '-'.")
            sys.exit(1)

    # Convert weights to float
    try:
        weights_list = [float(w) for w in weights_list]
    except ValueError:
        print("Error: Weights must be numeric values separated by comma.")
        sys.exit(1)

    return weights_list, impacts_list


def topsis(df, weights, impacts):
    data = df.iloc[:, 1:].values
    weights = np.array(weights)
    impacts = np.array(impacts)

    # Step 1: Normalize
    norm = np.sqrt((data ** 2).sum(axis=0))
    normalized = data / norm

    # Step 2: Weighted normalized matrix
    weighted = normalized * weights

    # Step 3: Ideal Best & Worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(np.max(weighted[:, i]))
            ideal_worst.append(np.min(weighted[:, i]))
        else:
            ideal_best.append(np.min(weighted[:, i]))
            ideal_worst.append(np.max(weighted[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distance calculation
    distance_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Performance Score
    score = distance_worst / (distance_best + distance_worst)

    return score


def main():
    input_file, weights, impacts, output_file = validate_input(sys.argv)

    try:
        df = pd.read_csv(input_file)
    except Exception:
        print("Error: Unable to read input file.")
        sys.exit(1)

    weights_list, impacts_list = validate_dataframe(df, weights, impacts)

    score = topsis(df, weights_list, impacts_list)

    df['Topsis Score'] = score
    df['Rank'] = df['Topsis Score'].rank(method='max', ascending=False).astype(int)

    df.to_csv(output_file, index=False)
    print("TOPSIS calculation completed successfully.")
    print(f"Result saved to {output_file}")


if __name__ == "__main__":
    main()
