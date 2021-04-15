from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import sklearn
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt





def load_iris_data():
    names=["sepal-length","sepal-width","petal-length","petal-width","class"]
    df=pd.read_csv(" EDK/klassifikasjons_prosjekt/Classification Iris/Iris_TTT4275/iris.data",names=names)

    fucked_train_df=pd.concat([df.iloc[:30],df.iloc[50:80],df.iloc[100:130]])
    fucked_test_df=pd.concat([df.iloc[30:50],df.iloc[80:100],df.iloc[130:150]])
    return fucked_train_df, fucked_test_df


train, test = load_iris_data()


def sigmoid(x_ik):
    return 1 / (1 + np.exp(-x_ik))


def class_to_vec(y):
    output = np.zeros(( 1,3))
    np.reshape(output,(3,1))
    #print(output[:,1])

    for i, val in enumerate(y):
        if "setosa" in val:
            np.append(output, np.reshape([1,0,0],(3,1)))
        elif "color" in val:
            np.append(output, np.reshape([0,1,0],(3,1)))
            
        else:
            np.append(output, np.reshape([0,0,1],(3,1)))
    print(output)
    quit()
    return output


def del_W_mse(g,t,x):
    ssum = 0
    N = t.shape[1]

    ting = ((g-t) * g * (1 - g)) @ x.T
    #print(ting)
    return np.sum(ting)


def mse(g,t):
    #print(g.T)
    print(g.T[0])
    #print(t.T)
    print(np.reshape(t.T[0],(3,1)))
    print(g.T[0]@np.reshape(t.T[0],(3,1)))
    quit()
    return np.sum((g - t) @ (g - t).T)


def aids_lin_classifier_training(train_data, test_data):
    
    x_train = train_data.iloc[:,:4]
    y_train = train_data.iloc[:,4]
    y_train = class_to_vec(y_train)
    y_train2 =np.zeros_like(y_train)
    
    #print(y_train.shape)
    print(mse(y_train, y_train2))
    #print(x_train)
    #print(y_train)
    x_train["intercept"] = 1
    #print(x_train)
    W = np.zeros((3,5))
    x_train = x_train.to_numpy()
   # print(x_train)
    
    alpha=1e-1
    for k in range(100):
        #print(W)
        #print(sigmoid(W @ x_train.T))
        W = W - alpha * del_W_mse(sigmoid(W @ x_train.T), y_train, x_train.T)
        print(mse(y_train, sigmoid(W @ x_train.T)))

aids_lin_classifier_training(train,test)










def scikit_learn(solution):
    X_train,X_test,Y_train,Y_test=sklearn.model_selection.train_test_split(df.loc[:,df.columns != "class"],df["class"],test_size=0.5)
    #print(X_train,Y_train)
    lda=LinearDiscriminantAnalysis()
    lda.fit(X_train,Y_train)
    preds=lda.predict(X_test)
    conf_matrix=sklearn.metrics.confusion_matrix(Y_test,preds)
    #print(conf_matrix)
