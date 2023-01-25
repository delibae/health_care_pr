from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import os
import pandas as pd

x_train = np.load(os.path.dirname(os.path.abspath(__file__)) + '/train/x_train.npy')
y_train = np.load(os.path.dirname(os.path.abspath(__file__)) + '/train/y_train.npy')
meta = np.load(os.path.dirname(os.path.abspath(__file__)) + '/train/meat.npy')

knn = KNeighborsClassifier(n_neighbors=25)
knn.fit(x_train , y_train)

head = meta[0]
mean = pd.Series(meta[1],dtype = float)
std = pd.Series(meta[2],dtype = float)




def predict_a(inp):

  inp = pd.DataFrame(inp,dtype = float)

  inp = (inp - mean)/std
  inp = np.array(inp)

  y_pred = knn.predict(inp)
  return int(y_pred.tolist()[0])


def get_head():
  return head

inp  = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
h = get_head()
print(h)

print(predict_a(inp))