
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt 
import numpy as np
from matplotlib import figure
from pandas import DataFrame

x_train, _ = make_blobs(n_samples= 500 , centers= 3,n_features =2, random_state= 20) 

'''# Generate a dataset with a random state of 42
X1, y1 = make_blobs(n_samples=100, random_state=42)

# Generate a different dataset with a different random state
X2, y2 = make_blobs(n_samples=100, random_state=123)

# X1 and X2 will be different because of the different random states
In this example, X1 and X2 will be different because we used different values for random_state. If we had used the same value for random_state, X1 and X2 would be the same.
'''
print(type(x_train))
print(x_train.shape)

df = DataFrame(dict(x= x_train[:, 0], y= x_train[:,1]))
fig, ax = plt.subplots(figsize =(8,8))
df.plot(ax =ax , kid = 'Scatter', x = "x", y = 'y')
plt.xlabel('x_1')
plt.ylabel('x_2')
pot.show()





 







