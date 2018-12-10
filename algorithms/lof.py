#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from sklearn.neighbors  import LocalOutlierFactor
import numpy as np

class lof(object):

    def __init__(self, n_neighbors=20,contamination = 0.01):
        self.n_neighbors = n_neighbors
        self.contamination = contamination

    def predict(self, X):
        """
        Predict if a particular sample is an outlier or not.
        :param X: the time series to detect of
        :param type X: pandas.Series
        :return: 0 denotes normal, 1 denotes abnormal
        """
        clf = LocalOutlierFactor(n_neighbors= self.n_neighbors, contamination= self.contamination)
        y_pred = clf.fit_predict(X)[-1]
        if y_pred > 0:
            return 0
        else:
            return 1