import torch
import numpy as np
from sklearn.preprocessing import LabelEncoder
import torch.nn.functional as F

PATH = '/projectnb/dl523/projects/trace_22/data/labelencoding.npy'

'''
Takes a list of vocab
'''
def train_label_encoding(vocab):
    le = LabelEncoder()
    ls = []
    for x in vocab:
        for item in x.strip().split():
            ls.append(item)
    le.fit(ls)

    return le

'''
Takes the string we want to onehot encode, the label encoder
'''

def train_onehot_encoding(X, le):
    X = X.split()
    X = torch.tensor(le.transform(X))
    return np.bitwise_or.reduce(F.one_hot(X, num_classes=126),axis=0)









