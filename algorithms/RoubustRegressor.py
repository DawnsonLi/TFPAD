#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
from sklearn.linear_model import HuberRegressor

class RoubustRegressor(object):
   
    def __init__(self):
        pass

    def predict(self, X, window = 180):
        """
        Predict if a particular sample is an outlier or not.
        :param X: the time series to detect of
        :param type X: numpy
        :param window: the length of window
        :param type window: int
        """
        x_train = list(range(0, 2 * window + 1)) + list(range(0, 2 * window + 1)) + list(range(0, window + 1))
        x_train = np.array(x_train)
        x_train = x_train[:, np.newaxis]
        avg_value = np.mean(X[-(window + 1):])
        if avg_value > 1:
            y_train = X / avg_value
        else:
            y_train = X
        #y = X.reshape(-1, 1) 
        model = HuberRegressor().fit(x_train, y_train)
        return model.predict(x_train)
