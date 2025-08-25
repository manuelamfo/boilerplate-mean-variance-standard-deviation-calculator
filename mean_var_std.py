import numpy as np

def calculate(list):
    matrix = np.array([[list[0:3]],[list[3:6]],[list[6:9]]])
    mean_x_axis_matrix = matrix.mean(axis=0)
    mean_y_axis_matrix = matrix.mean(axis=1)
    mean_matrix = matrix.mean()

    print(f"mean x: {mean_x_axis_matrix}, mean y:{mean_y_axis_matrix}, mean across x and y:{mean_matrix}\n")

    calculations = {'mean': [mean_x_axis_matrix], [mean_y_axis_matrix], [mean_matrix]}
    return calculations