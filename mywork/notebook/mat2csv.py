import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class MatCsvPathPair:
    def __init__(self,
                 root="../../project/main/",
                 objects="objects/",
                 relations="matrices/",
                 SAME_MODE_output="output_s/",
                 DIFF_MODE_output="output_d/"):
        self.root = root
        self.objects = root+objects  # ../../project/main/objects/
        self.relations = root+relations  # ../../project/main/matrices/
        self.SAME_MODE_output = root+SAME_MODE_output  # ../../project/main/output_s/
        self.DIFF_MODE_output = root+DIFF_MODE_output  # ../../project/main/output_d/
        print("MatCsvPathPair avaliable path:")
        print()
        print("        " + root)
        print("          " + objects)
        print("            - objectA.mat")
        print("            - objectB.mat")
        print("            - objectC.mat")
        print("          " + relations)
        print("            - R1-2.mat")
        print("            - T1-1.mat")
        print("          " + SAME_MODE_output)
        print("            - new_found_relations.mat")
        print("          " + DIFF_MODE_output)
        print("            - new_found_relations_row.mat")
        print("            - new_found_relations_col.mat")
        print()

    def getOriginalRelationPair(self, name="R1-3"):
        return (self.relations+'{}.mat'.format(name), "./{}.csv".format(name))

    def getObjectPair(self, name="objectA"):
        return (self.objects+'{}.mat'.format(name), "./{}.csv".format(name))

    def getSAME_NewFoundRelationPair(self, name="new_found_relations"):
        return (self.SAME_MODE_output+'{}.csv'.format(name), "./{}.csv".format(name))

    def getDIFF_NewFoundRelationPair(self, name="new_found_relations_row"):
        return (self.DIFF_MODE_output+'{}.csv'.format(name), "./{}.csv".format(name))


############################ object ############################


def load_object(mat_path, key="vett"):
    """加载mat_path文件中标签为key的那个矩阵，返回构造好的DataFrame
    """
    matrix = sio.loadmat(mat_path)[key]
    new_matrix = []
    for i in matrix:
        new_matrix.append(i[0][0])
    return pd.DataFrame(new_matrix)


def save_Object_mat_to_csv(mat_path, output_path):
    df_matrix = load_object(mat_path)
    df_matrix.to_csv(output_path)

############################ original relation ############################


def load_relation(key, path):
    matrix = sio.loadmat(path)[key].todense()
    matrix_data = []
    for i in np.asarray(matrix):
        matrix_data.append([j for j in i])
    return pd.DataFrame(matrix_data)


def save_mat_to_csv(key, path, output_path):
    df_matrix = load_relation(key, path)
    df_matrix.to_csv(output_path)


def save_OriginalR_mat_to_csv(path='../../project/main/matrices/R1-3.mat', output_path="./R.csv"):
    save_mat_to_csv("R_matr", path, output_path)


def save_OriginalTheta_mat_to_csv(path='../../project/main/matrices/T1-1.mat', output_path="./T1-1.csv"):
    save_mat_to_csv("teta_matr", path, output_path)

############################ new_found_relation ############################


def load_new_found_relation(idx_obj_path, col_obj_path, relation_path):
    pd_idx = list(load_object(idx_obj_path)[0])
    pd_col = list(load_object(col_obj_path)[0])
    pd_complete = pd.DataFrame(data=[[0.0]*len(pd_col)]*len(pd_idx), index=pd_idx, columns=pd_col)
    with open(relation_path, "r") as F:
        for i in F.readlines():
            ap = i.split(',')
            key_x = ap[0]
            key_y = ap[1]
            value = float(ap[2])
            pd_complete[key_y][key_x] = value
    return pd_complete


def save_new_found_relations_mat_to_csv(
        idx_obj_path='../../project/main/objects/objectB.mat',
        col_obj_path='../../project/main/objects/objectA.mat',
        relation_path='../../project/main/output_d/new_found_relations_row.csv',
        output_path="./new_found_relations.csv"):
    pd_complete = load_new_found_relation(idx_obj_path, col_obj_path, relation_path)
    pd_complete.to_csv(output_path)


def save_SAME_MODE_new_found_relations_mat_to_csv(
        idx_obj_path='../../project/main/objects/objectA.mat',
        relation_path='../../project/main/output_s/new_found_relations.csv',
        output_path="./new_found_relations.csv"):
    save_new_found_relations_mat_to_csv(idx_obj_path, idx_obj_path, relation_path, output_path)


def save_DIFF_MODE_new_found_relations_mat_to_csv(
        idx_obj_path='../../project/main/objects/objectB.mat',
        col_obj_path='../../project/main/objects/objectA.mat',
        relation_path='../../project/main/output_d/new_found_relations_row.csv',
        output_path="./new_found_relations.csv"):
    save_new_found_relations_mat_to_csv(idx_obj_path, col_obj_path, relation_path, output_path)


class DataManager:
    def __init__(self):
        print("DataManager avaliable method :")
        print("""
        load:
            object -> (obj_mat_path)
            relation -> (key, path)
            new_found_relation -> (idx_obj_path, col_obj_path, relation_path)

        save:
            object -> (in_path, out_path)
            R_relation, T_relation  -> (in_path, out_path)
            SAME_new_found_relation -> (idx_obj_path, in_path, out_path)
            DIFF_new_found_relation -> (idx_obj_path, col_obj_path, in_path, out_path)

        save_all
        """)

    def load(self, method="object"):
        if method == "object":
            return load_object
        elif method == "relation":
            return load_relation
        elif method == "new_found_relation":
            return load_new_found_relation
        else:
            raise NotImplementedError("Method Not Found")

    def save(self, method="object"):
        if method == "object":
            return save_Object_mat_to_csv
        elif method == "R_relation":
            return save_OriginalR_mat_to_csv
        elif method == "T_relation":
            return save_OriginalTheta_mat_to_csv
        elif method == "SAME_new_found_relation":
            return save_SAME_MODE_new_found_relations_mat_to_csv
        elif method == "DIFF_new_found_relation":
            return save_DIFF_MODE_new_found_relations_mat_to_csv
        else:
            raise NotImplementedError("Method Not Found")

    def save_all(self):
        save_Object_mat_to_csv('../../project/main/objects/objectA.mat', "./objectA.csv")
        save_Object_mat_to_csv('../../project/main/objects/objectB.mat', "./objectB.csv")
        save_Object_mat_to_csv('../../project/main/objects/objectC.mat', "./objectC.csv")

        save_OriginalR_mat_to_csv('../../project/main/matrices/R1-3.mat', "./R1-3.csv")
        save_OriginalTheta_mat_to_csv('../../project/main/matrices/T1-1.mat', "./T1-1.csv")

        save_SAME_MODE_new_found_relations_mat_to_csv(
            idx_obj_path='../../project/main/objects/objectA.mat',
            relation_path='../../project/main/output_s/new_found_relations.csv',
            output_path="./new_found_relations.csv")
        save_DIFF_MODE_new_found_relations_mat_to_csv(
            idx_obj_path='../../project/main/objects/objectB.mat',
            col_obj_path='../../project/main/objects/objectA.mat',
            relation_path='../../project/main/output_d/new_found_relations_row.csv',
            output_path="./new_found_relations_row.csv")
        save_DIFF_MODE_new_found_relations_mat_to_csv(
            idx_obj_path='../../project/main/objects/objectB.mat',
            col_obj_path='../../project/main/objects/objectA.mat',
            relation_path='../../project/main/output_d/new_found_relations_col.csv',
            output_path="./new_found_relations_col.csv")
