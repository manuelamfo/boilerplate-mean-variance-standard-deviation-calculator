import numpy as np

def calculate(list):
    if(len(list) < 9):
        raise ValueError("List must contain nine numbers.")

    matrix = np.array([list[0:3], list[3:6], list[6:9]])
    mean_axis0 = np.mean(matrix, axis=0)
    mean_axis1 = np.mean(matrix, axis=1)
    mean_elemen = np.mean(matrix)

    variance_axis0 = np.var(matrix,axis=0)
    variance_axis1 = np.var(matrix, axis=1)
    variance_elemen = np.var(matrix)

    std_dev_axis0 = np.std(matrix, axis=0)
    std_dev_axis1 = np.std(matrix, axis=1)
    std_dev_elemen = np.std(matrix)

    max_axis0 = np.max(matrix, axis=0)
    max_axis1 = np.max(matrix, axis=1)
    max_elemen = np.max(matrix)

    min_axis0 = np.min(matrix, axis=0)
    min_axis1= np.min(matrix,axis=1)
    min_elemen = np.min(matrix)

    sum_axis0 = np.sum(matrix, axis=0)
    sum_axis1 = np.sum(matrix, axis=1)
    sum_elemen = np.sum(matrix)

    mean_list = [mean_axis0.tolist(), mean_axis1.tolist(), mean_elemen]
    variance_list = [variance_axis0.tolist(), variance_axis1.tolist(), variance_elemen]
    std_dev_list = [std_dev_axis0.tolist(), std_dev_axis1.tolist(), std_dev_elemen]
    max_list = [max_axis0.tolist(), max_axis1.tolist(), max_elemen]
    min_list = [min_axis0.tolist(), min_axis1.tolist(), min_elemen]
    sum_list = [sum_axis0.tolist(), sum_axis1.tolist(), sum_elemen]

    calculations = {'mean': mean_list, 
                    'variance': variance_list, 
                    'standard deviation': std_dev_list,
                    'max': max_list,
                    'min': min_list,
                    'sum': sum_list}
    return calculations