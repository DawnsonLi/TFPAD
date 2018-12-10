#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from algorithms.ewma import Ewma
from algorithms.ksigma import ksigma
from algorithms.lof import lof
def ewma_residual_ksigma(X_formal):
    """
    :param X_formal: formal time series
    :param type X: numpy
    :return: 1 denotes normal, 0 denotes abnormal
    """
    e_pre = Ewma()
    s = e_pre.predict_all(X_formal)
    residual = X_formal - s
    k = ksigma()
    return k.predict(residual)

def ewma_residual_lof(X_formal):
    """
    :param X_formal: formal time series
    :param type X: numpy
    :return: 1 denotes normal, 0 denotes abnormal
    """
    e_pre = Ewma()
    s = e_pre.predict_all(X_formal)
    residual = X_formal - s
    #print residual
    l = lof()
    residual = residual.reshape(-1, 1)
    return l.predict(residual)

