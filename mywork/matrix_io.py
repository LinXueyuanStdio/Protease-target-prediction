
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def save_matrix(matrix, path):
    matrix_data = []
    for i in np.asarray(matrix):
        matrix_data.append([j for j in i])
    df_matrix = pd.DataFrame(matrix_data)
    df_matrix.to_csv(path)


def save_R_mat_to_csv(matPath='../../project/main/matrices/R1-3.mat', output_path="./R.csv"):
    Rmatrix = sio.loadmat(matPath)["R_attr"].todense()
    save_matrix(Rmatrix, output_path)


def save_Object_mat_to_csv(matPath='../../project/main/objects/objectA.mat', output_path="./objectA.csv"):
    Rmatrix = sio.loadmat(matPath)["vett"].todense()
    save_matrix(Rmatrix, output_path)
