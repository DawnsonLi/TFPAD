# -*- coding: utf-8 -*-
def evalute_delay(real, predict, delay = 7):
    counter = 0#记录异常片段的长度
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    find = False
    for i in range(len(predict)):
        if real[i] == 0:#正常数据
            if find:
                tp += counter
                counter = 0
                find = False
            else:
                fn += counter
                counter = 0              
            if predict[i] == 0:
                tn += 1
            else:
                fp += 1
        else:
            if predict[i] != 0 and counter <= delay:
                find = True
            counter += 1
            #print counter
    if counter > 0 and find:#处理尾部是异常的情况
        tp += counter  
    if counter >0 and find == False:
        fn += counter
    
    print 'tp:',tp  
    print 'tn:',tn 
    print 'fp:',fp 
    print 'fn:',fn  
    precison = tp*1.0/(tp+fp)
    recall = tp*1.0/(tp+fn)
    if tp ==0:
        f1 = 0
    else:
        f1 = 2*precison*recall/(precison+recall)
    print 'precison:',precison
    print 'recall:',recall
    print 'f1 score:',f1
    return tp,tn,fp,fn ,precison, recall,f1