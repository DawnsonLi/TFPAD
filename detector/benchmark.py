#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from algorithms.ewma import Ewma
from algorithms import ewmaResidual
from algorithms import polyResidual
from algorithms import roubustResidual
from algorithms.TSlist import TSlist
from evalute import evalute_delay
import pandas as pd
import numpy as np

def benchmark_poly_ksigma(num):
    file_name = 'E:/javacode/AIOPS/data/series/'
    log = []
    print num
    train = pd.read_csv(file_name+num+'_train.csv')
    t = TSlist(train)
    test = pd.read_csv(file_name+num+'_test.csv')
    t.append_df(test)
    t.fill_missed_median()
    timestamp = test['timestamp'].values
    span = timestamp[1] - timestamp[0]
    y = []
    w = 3600*3/span
    print 'sample num in each hour:',w/3
    for i in range(1,len(timestamp)):
        if i % 5000 == 0:
            print i*100.0/len(timestamp),"%"
        #构造数据块
        w_now = t.get_series(timestamp[i], w+1)
        yest_stamp = timestamp[i] - 24*3600
        w_yest1 = t.get_series(yest_stamp, w+1)
        yest_stamp2 = timestamp[i] - 24*3600 + 3600*3#后移三个小时
        w_yest2 = t.get_series(yest_stamp2, w)
        last_week = timestamp[i] - 24*3600*7
        w_last_week1 = t.get_series(last_week, w+1)
        last_week2 = timestamp[i] - 24*3600*7 + 3600*3
        w_last_week2 = t.get_series(last_week2, w)
    
        w_yest1.extend(w_yest2)
        w_last_week1.extend(w_last_week2)
        w_last_week1.extend(w_yest1)
        w_last_week1.extend(w_now)
        X_formal = np.array(w_last_week1) 
        #algorithm
        ans = polyResidual.poly_residual_ksigma(X_formal,w)
        #ans = ewmaResidual.ewma_residual_ksigma(X_formal)
        #ans = ewmaResidual.ewma_residual_lof(X_formal)
        y.append(ans)
    tp,tn,fp,fn ,precison, recall,f1= evalute_delay(test['label'], y, delay = 7)
    log.append([num, precison, recall, f1])
    log = pd.DataFrame(log, columns=['kpi id','precison','recall','fscore'])
    #log.to_csv('log/'+str(num)+' ewma_lof.csv')
    log.to_csv('log/'+str(num)+' poly_ksigma.csv')
       
def benchmark_poly_lof(num):
    file_name = 'E:/javacode/AIOPS/data/series/'
    log = []
    print num
    train = pd.read_csv(file_name+num+'_train.csv')
    t = TSlist(train)
    test = pd.read_csv(file_name+num+'_test.csv')
    t.append_df(test)
    t.fill_missed_median()
    timestamp = test['timestamp'].values
    span = timestamp[1] - timestamp[0]
    y = []
    w = 3600*3/span
    print 'sample num in each hour:',w/3
    for i in range(1,len(timestamp)):
        if i % 5000 == 0:
            print i*100.0/len(timestamp),"%"
        #构造数据块
        w_now = t.get_series(timestamp[i], w+1)
        yest_stamp = timestamp[i] - 24*3600
        w_yest1 = t.get_series(yest_stamp, w+1)
        yest_stamp2 = timestamp[i] - 24*3600 + 3600*3#后移三个小时
        w_yest2 = t.get_series(yest_stamp2, w)
        last_week = timestamp[i] - 24*3600*7
        w_last_week1 = t.get_series(last_week, w+1)
        last_week2 = timestamp[i] - 24*3600*7 + 3600*3
        w_last_week2 = t.get_series(last_week2, w)
    
        w_yest1.extend(w_yest2)
        w_last_week1.extend(w_last_week2)
        w_last_week1.extend(w_yest1)
        w_last_week1.extend(w_now)
        X_formal = np.array(w_last_week1) 
        #algorithm
        ans = polyResidual.poly_residual_lof(X_formal,w)
        #ans = ewmaResidual.ewma_residual_ksigma(X_formal)
        #ans = ewmaResidual.ewma_residual_lof(X_formal)
        y.append(ans)
    tp,tn,fp,fn ,precison, recall,f1= evalute_delay(test['label'], y, delay = 7)
    log.append([num, precison, recall, f1])
    log = pd.DataFrame(log, columns=['kpi id','precison','recall','fscore'])
    #log.to_csv('log/'+str(num)+' ewma_lof.csv')
    log.to_csv('log/'+str(num)+' poly_lof.csv')

def benchmark_roubust_ksigma(num):
    file_name = 'E:/javacode/AIOPS/data/series/'
    log = []
    print num
    train = pd.read_csv(file_name+num+'_train.csv')
    t = TSlist(train)
    test = pd.read_csv(file_name+num+'_test.csv')
    t.append_df(test)
    t.fill_missed_median()
    timestamp = test['timestamp'].values
    span = timestamp[1] - timestamp[0]
    y = []
    w = 3600*3/span
    print 'sample num in each hour:',w/3
    for i in range(1,len(timestamp)):
        if i % 5000 == 0:
            print i*100.0/len(timestamp),"%"
        #构造数据块
        w_now = t.get_series(timestamp[i], w+1)
        yest_stamp = timestamp[i] - 24*3600
        w_yest1 = t.get_series(yest_stamp, w+1)
        yest_stamp2 = timestamp[i] - 24*3600 + 3600*3#后移三个小时
        w_yest2 = t.get_series(yest_stamp2, w)
        last_week = timestamp[i] - 24*3600*7
        w_last_week1 = t.get_series(last_week, w+1)
        last_week2 = timestamp[i] - 24*3600*7 + 3600*3
        w_last_week2 = t.get_series(last_week2, w)
    
        w_yest1.extend(w_yest2)
        w_last_week1.extend(w_last_week2)
        w_last_week1.extend(w_yest1)
        w_last_week1.extend(w_now)
        X_formal = np.array(w_last_week1) 
        #algorithm
        ans = roubustResidual.roubust_residual_ksigma(X_formal,w)
        #ans = ewmaResidual.ewma_residual_ksigma(X_formal)
        #ans = ewmaResidual.ewma_residual_lof(X_formal)
        y.append(ans)
    tp,tn,fp,fn ,precison, recall,f1= evalute_delay(test['label'], y, delay = 7)
    log.append([num, tp,tn,fp,fn, precison, recall, f1])
    log = pd.DataFrame(log, columns=['kpi id','tp','tn','fp','fn','precison','recall','fscore'])
    #log.to_csv('log/'+str(num)+' ewma_lof.csv')
    log.to_csv('log/'+str(num)+' roubust_ksigma.csv')
