import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def knn(x, X, Y, k=1):
    return Y[np.sum((X - x) ** 2, axis=1).argmin()]

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(url, header=None)
X = df.iloc[:, :4].values
Y = df.iloc[:, -1].values
classes = np.unique(Y)
# colors = dict(zip(classes, ['.r', '.g', '.b']))
# for c in classes:
#     idx = Y == c
#     plt.plot(X[idx, 0], X[idx, 2], colors[c])
# plt.show()
itrain = np.r_[0:25, 50:75, 100:125]
itest = np.r_[25:50, 75:100, 125:150]
Xtrain, Ytrain = X[itrain], Y[itrain]
Xtest, Ytest = X[itest], Y[itest]
correct = 0
for x, y in zip(Xtest, Ytest):
    z = knn(x, Xtrain, Ytrain)
    if z == y:
        correct += 1
print(f'accuracy rate: {correct/len(Xtest)*100:.2f}')
