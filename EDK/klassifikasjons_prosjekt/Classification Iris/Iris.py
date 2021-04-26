from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import sklearn
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as la




def load_iris_data(cutvals=None):
    names = ["sepal-length","sepal-width","petal-length","petal-width","class"]
    df = pd.read_csv("EDK/klassifikasjons_prosjekt/Classification Iris/Iris_TTT4275/iris.data", names=names)

    fucked_train_df = pd.concat([df.iloc[:30], df.iloc[50:80], df.iloc[100:130]])
    fucked_test_df = pd.concat([df.iloc[30:50], df.iloc[80:100], df.iloc[130:150]])

    other_fucked_train_df = pd.concat([df.iloc[20:50], df.iloc[70:100], df.iloc[120:]])
    other_fucked_test_df = pd.concat([df.iloc[:20], df.iloc[50:70], df.iloc[100:120]])
    if cutvals:
        return fucked_train_df.drop(cutvals,axis=1), fucked_test_df.drop(cutvals,axis=1), other_fucked_train_df.drop(cutvals,axis=1), other_fucked_test_df.drop(cutvals,axis=1)


    return fucked_train_df, fucked_test_df, other_fucked_train_df, other_fucked_test_df




def sigmoid(x_ik):
    return 1 / (1 + np.exp(-x_ik))


def class_to_vec(y):
    output = np.zeros((3, y.shape[0]))
    for i, val in enumerate(y):
        if "setosa" in val:
            output[0, i] = 1
        elif "color" in val:
            output[1, i] = 1
        else:
            output[2, i] = 1
    return output


def del_W_mse(g,t,x):
    return ((g-t) * g * (1 - g)) @ x.T
 


def mse(g, t):
    error = g - t
    ssum = 0
    for err in error:
        ssum += la.norm(err)
    return ssum


def confusion_matrix(estimate, target, n_per_class):
    matrix=np.zeros((3,3))
    estimate=estimate.T
    target=target.T
    p=0
    true_c1, true_c2, true_c3 = target[:n_per_class], target[n_per_class:2 * n_per_class], target[2*n_per_class:]
    est_c1, est_c2, est_c3 = estimate[:n_per_class], estimate[n_per_class:2 * n_per_class], estimate[2*n_per_class:]
    if p:
        print(true_c1)
        print(est_c1)
        print(true_c2)
        print(est_c2)
        print(true_c3)
        print(est_c3)
        
    for g,t in zip(est_c1, true_c1):
        if list(g) == list(t): # hvis trodde c1 og d var c1
            matrix[0, 0] += 1
        if list(g) == [0, 1, 0]: # hvis trodde d var c2 og d var c1
            matrix[1, 0] += 1
        if list(g) == [0, 0, 1]: #hvis trodde d var c3 og d var c1
            matrix[2, 0] += 1
    
    for g,t in zip(est_c2,true_c2):
        if list(g) == list(t): # hvis trodde c2 og d var c2
            matrix[1, 1] += 1
        if list(g) == [1, 0, 0]: # hvis trodde c1 og d var c2
            matrix[0, 1] += 1
        if list(g) == [0, 0, 1]: # hvis trodde c3 og d var c2
            matrix[2, 1] += 1
    
    for g,t in zip(est_c3,true_c3):
        if list(g) == list(t): # hvis den trodde det var c3 og det var c3
            matrix[2, 2] += 1
        if list(g) == [1, 0, 0]: #hvis den trodde det var c1 men den var c3
            matrix[0, 2] += 1
        if list(g) == [0, 1, 0]: # hvis den trodde d var c2 men d var c3
            matrix[1, 2] += 1
    print(matrix)
    return matrix


def classify(vec):
        output = np.zeros_like(vec.T)
        for i, pred in enumerate(vec.T):
            if np.argmax(pred) == 0:
                output[i, 0] = 1
            elif np.argmax(pred) == 1 :
                output[i, 1] = 1
            else:
                output[i, 2] = 1
        return output.T 
    

def aids_lin_classifier(train_data, test_data,alpha):
   # print(train_data)
    x_train, y_train= train_data.iloc[:, :-1], class_to_vec(train_data.iloc[:, -1])
    x_train["intercept"] = 1
    x_train = x_train.to_numpy().T


    x_test, y_test = test_data.iloc[:, :-1], class_to_vec(test_data.iloc[:, -1])
    x_test["intercept"] = 1
    W = np.random.rand(3, x_train.shape[0])

   
  
  #alpha =0.01 funker høvelig
    for _ in range(10000):
        W = W - alpha * del_W_mse(sigmoid(W @ x_train), y_train, x_train)
    
    res = sigmoid(W@x_test.to_numpy().T)
    return confusion_matrix(classify(res), y_test, 20)





def plot_features(df1, df2, df3):
    k=20
    for col in df1.columns:
        fig, axs = plt.subplots(1, 3,sharey=True, sharex=True)

        # We can set the number of bins with the `bins` kwarg
        
        axs[0].hist(df1[col], color="C0", label="Setosa",bins=k)
        axs[1].hist(df2[col], color="C1", label="Versicolor",bins=k)
        axs[2].hist(df3[col], color="C2", label="Virginica",bins=k)
        axs[0].legend()
        axs[1].legend()
        axs[2].legend()
        plt.suptitle(col)
        plt.savefig(f"EDK/klassifikasjons_prosjekt/figs/feature_histogram_class_separated_{col}.pdf")
    #plt.show()
    k2=40
    fulldf=pd.concat((df1, df2, df3))
    for col in fulldf.columns:
        plt.figure()
        plt.hist(fulldf[col], label=col, bins=k2)
        plt.show()



names = ["sepal-length","sepal-width","petal-length","petal-width"]
dfs = [pd.read_csv(f"EDK/klassifikasjons_prosjekt/Classification Iris/Iris_TTT4275/class_{i}", names=names) for i in range(1,4)]
df1, df2, df3 = dfs


train, test, train2, test2 = load_iris_data()
train_3pred, test_3pred, train2_3pred, test2_3pred = load_iris_data("sepal-width")
train_2pred, test_2pred, train2_2pred, test2_2pred = load_iris_data(["sepal-width", "sepal-length"])
train_1pred, test_1pred, train2_1pred, test2_1pred = load_iris_data(["sepal-width", "sepal-length", "petal-length",])

print(f"Test confusion matriix, {train.columns}, first 30 set:")
aids_lin_classifier(train, test, 0.02)

print(f"Test confusion matrix, {train2.columns}, last 30 set:")
aids_lin_classifier(train2, test2, 0.02)

print(f"Test confusion matriix, {train_3pred.columns}, first 30 set:")
aids_lin_classifier(train_3pred, test_3pred, 0.02)

print(f"Test confusion matrix, {train2_3pred.columns}, last 30 set:")
aids_lin_classifier(train2_3pred, test2_3pred, 0.02)

print(f"Test confusion matriix,  {train_2pred.columns}, first 30 set:")
aids_lin_classifier(train_2pred, test_2pred, 0.02)

print(f"Test confusion matrix, {train2_2pred.columns}, last 30 set:")
aids_lin_classifier(train2_2pred, test2_2pred, 0.02)

print(f"Test confusion matriix, {train_1pred.columns}, first 30 set:")
aids_lin_classifier(train_1pred, test_1pred, 0.02)

print(f"Test confusion matrix,{train2_1pred.columns}, last 30 set:")
aids_lin_classifier(train2_1pred, test2_1pred, 0.02)

plot_features(df1, df2, df3)