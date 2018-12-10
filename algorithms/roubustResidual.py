#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from algorithms.ksigma import ksigma
from algorithms.lof import lof
from algorithms.RoubustRegressor import RoubustRegressor
def roubust_residual_ksigma(X_formal, window=180):
    """
    :param X_formal: formal time series
    :param type X: numpy
    :return: 0 denotes normal, 1 denotes abnormal
    """
    pre = RoubustRegressor()
    s = pre.predict(X_formal, window)
    residual = X_formal - s
    if residual[-1] < 0.00001:
        return 0
    else:
        k = ksigma()
        return k.predict(residual)

def roubust_residual_lof(X_formal,  window=180):
    """
    :param X_formal: formal time series
    :param type X: numpy
    :return: 0 denotes normal, 1 denotes abnormal
    """
    pre = RoubustRegressor()
    s = pre.predict(X_formal, window)
    residual = X_formal - s
    l = lof()
    residual = residual.reshape(-1, 1)
    return l.predict(residual)

