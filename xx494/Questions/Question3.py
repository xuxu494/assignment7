'''
Created on Nov 2, 2015

@author: ds-ga-1007
'''
import numpy as np

def question3():
    a = np.random.random(30).reshape(10,3) #generate the 10X3 array
    b = np.argsort(np.abs(a-0.5))
    c = b[:, 0.1].ravel().tolist()
    d = a[np.arange(a.shape[0]), c]
    print d