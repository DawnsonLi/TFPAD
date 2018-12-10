#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np

class ksigma(object):

    def __init__(self, index=3):
        """
        :param index: multiple of standard deviation
        :param type: int or float
        """
        self.index = index

    def predict(self, X):
        """
        Predict if a particular sample is an outlier or not.

        :param X: the time series to detect of
        :param type X: pandas.Series
        :return: 0 denotes normal, 1 denotes abnormal
        """
        if abs(X[-1] - np.mean(X[:-1])) > self.index * np.std(X[:-1]):
            return 1
        return 0
    