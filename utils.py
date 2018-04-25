
# coding: utf-8

import numpy as np
import h5py

def read_data(filename):
    f = open(filename)
    lines = f.readlines()
    lines = map(lambda x:x.strip() , lines)
    data = map(lambda x:x.split(',') ,lines)
    data = list(data)
    data = np.array(data,dtype=np.float)
    return data


def write_dataset(dbName,features,labels):
    try:
        f = h5py.File(dbName,"w")
        f.create_dataset("X",data = features)
        f.create_dataset("Y",data = labels)
    finally:
        f.close()

def load(dbName):
    try:
        f = h5py.File(dbName,"r")
        X = f['X'][:]
        Y = f['Y'][:]
    finally:
        f.close()
    return X,Y