#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from algorithms.polynomial_interpolation import PolynomialInterpolation
from algorithms.ksigma import ksigma
from algorithms.lof import lof
def poly_residual_ksigma(X_formal, window=180):
    """
    :param X_formal: formal time series
    :param type X: numpy
    :return: 0 denotes normal, 1 denotes abnormal
    """
    pre = PolynomialInterpolation()
    s = pre.predict(X_formal, window)
    residual = X_formal - s
    k = ksigma()
    return k.predict(residual)

def poly_residual_lof(X_formal,  window=180):
    """
    :param X_formal: formal time series
    :param type X: numpy
    :return: 0 denotes normal, 1 denotes abnormal
    """
    pre = PolynomialInterpolation()
    s = pre.predict(X_formal, window)
    residual = X_formal - s
    l = lof()
    residual = residual.reshape(-1, 1)
    return l.predict(residual)

