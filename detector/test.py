#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from benchmark import benchmark_poly_ksigma
from benchmark import benchmark_roubust_ksigma
numbers = ['27']
#numbers = ['2','6','7','10','14','19','26','27']
for num in numbers:
    benchmark_roubust_ksigma(num)