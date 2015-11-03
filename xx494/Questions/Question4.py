'''
Created on Nov 2, 2015

@author: ds-ga-1007
'''
import numpy as np
import matplotlib.pyplot as plt

def question4():
    N_max = 50
    some_threshold = 50 
    
    x1 = np.linspace(-2, 1, 1000 )
    y1 = np.linspace(-1.5, 1.5, 1000)
    x,y = np.meshgrid(x1, y1)
    
    c = x + 1j*y
    z = c
    for v in range(N_max):
        z = z**2 + c
    
    mask = (np.abs(z) < some_threshold)
    plt.imshow(mask, extent = [-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
        
    
    