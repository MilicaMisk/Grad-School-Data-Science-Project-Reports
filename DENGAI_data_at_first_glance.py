import pandas as pd
import numpy as np
import tensorflow as tf

from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split


train_features = pd.read_csv('/home/milica/Desktop/competition 2/data/dengue_features_train.csv', index_col=[0,1,2])
train_labels = pd.read_csv('/home/milica/Desktop/competition 2/data/dengue_labels_train.csv', index_col=[0,1,2])

sj_train_features = train_features.loc['sj']
sj_train_labels = train_labels.loc['sj']

iq_train_features = train_features.loc['iq']
iq_train_labels = train_labels.loc['iq']

# fig = plt.figure()
# ax = fig.add_subplot(111)
# sj_train_labels.plot(color='green')
# iq_train_labels.plot(color='purple',secondary_y=True)
# plt.show()

# print(sj_train_labels)
train_labels.plot()
plt.show()