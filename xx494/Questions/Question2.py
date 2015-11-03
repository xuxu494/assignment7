'''
Created on Nov 2, 2015

@author: ds-ga-1007
'''
import numpy as np

def question2():
    a = np.arange(25).reshape(5,5)
    b = np.array([1.,5, 10, 15, 20])
    c = (a.T/b).T
    print c 
    