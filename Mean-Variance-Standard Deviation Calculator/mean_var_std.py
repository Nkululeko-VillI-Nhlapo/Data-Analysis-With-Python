# Mean-Variance-Standard Deviation Calculator
import numpy as np

def calculate(lst):
    # Check if the input list contains exactly 9 elements
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the input list into a 3x3 NumPy array
    matrix = np.array(lst).reshape(3, 3)
    
    # Calculate the required statistics along the specified axes and for the flattened matrix
    mean_axis0 = matrix.mean(axis=0).tolist()
    mean_axis1 = matrix.mean(axis=1).tolist()
    mean_flattened = matrix.mean().tolist()

    var_axis0 = matrix.var(axis=0).tolist()
    var_axis1 = matrix.var(axis=1).tolist()
    var_flattened = matrix.var().tolist()

    std_axis0 = matrix.std(axis=0).tolist()
    std_axis1 = matrix.std(axis=1).tolist()
    std_flattened = matrix.std().tolist()

    max_axis0 = matrix.max(axis=0).tolist()
    max_axis1 = matrix.max(axis=1).tolist()
    max_flattened = matrix.max().tolist()

    min_axis0 = matrix.min(axis=0).tolist()
    min_axis1 = matrix.min(axis=1).tolist()
    min_flattened = matrix.min().tolist()

    sum_axis0 = matrix.sum(axis=0).tolist()
    sum_axis1 = matrix.sum(axis=1).tolist()
    sum_flattened = matrix.sum().tolist()

    # Create a dictionary to store the results in a structured format
    calculations = {
        'mean': [mean_axis0, mean_axis1, mean_flattened],
        'variance': [var_axis0, var_axis1, var_flattened],
        'standard deviation': [std_axis0, std_axis1, std_flattened],
        'max': [max_axis0, max_axis1, max_flattened],
        'min': [min_axis0, min_axis1, min_flattened],
        'sum': [sum_axis0, sum_axis1, sum_flattened]
    }

    # Return the structured dictionary with the results
    return calculations
