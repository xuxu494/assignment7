'''
Created on Nov 2, 2015

@author: ds-ga-1007
'''
import numpy as np

def question1():
    #create the array
    a = np.arange(1,16).reshape(3, 5).T
    
    #generate a new array containing the 2nd and 4th rows
    a_a = a[np.array([1,3])]
    print 'The new array contains the 2nd and 4th rows is \n', a_a
    
    #generate a new array that contains the 2nd column
    a_b = a[:, 1]
    print 'The new array contains the 2nd column is \n', a_b
    
    #generate a new array that contains all the elements in the rectangular 
    #section between the coordinates [1,0] and [3,2]
    a_c = a[np.arange(1,4)]
    print 'The new array contains all the elements in the rectangular section between the coordates [1,0] and [3,2] is \n', a_c
    
    #generate a new array that contains only elements with values that are between 3 nd 11
    a_d = np.array([i for i in a.flat if 2<i<12])
    print "The new array contains only elements with value that are between 3 and 12 \n", a_d