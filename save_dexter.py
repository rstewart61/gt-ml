#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:44:23 2020

@author: brandon
"""

from skhubness.data import load_dexter
import pandas as pd
import numpy as np
import scipy.sparse

def dexter():
    X, y = load_dexter()
    print(X)
    print(y)
    y = y.astype(np.int64)
    y[y == -1] = 0
    print(y)
    print('Dexter bin counts', np.bincount(y))
    # TODO:
    # pd.to_csv()
    return X, y

def save_dexter():
    X, y = dexter()
    all_data = np.concatenate((X, y.reshape(-1, 1)), axis=1)
    sparse = scipy.sparse.csc_matrix(all_data)
    scipy.sparse.save_npz('data/dexter/dexter.npz', sparse)
    df = pd.DataFrame(all_data)
    df.to_csv('data/dexter/dexter.csv')

if __name__ == "__main__":
    save_dexter()