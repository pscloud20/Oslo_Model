# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:48:50 2022

@author: PSClo
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from numpy.random import default_rng
import tqdm

#%%

#defining site 1 in mathematical oslo model as site 0

class oslo:
    
    def __init__(self, L, prob): #calling class objects length of model and probability
        self.__L = L 
        self.__prob = p
        self.__z = np.zeros(L) #initialise array length L that contains slopes at each site (initially 0 will add values later)
        self.__h = np.zeros(L) #same for heights as slopes
        self.__threshold = t_z
        
    def drive(self): #define a drive function for when adding a grain 
        self.__z[0] = self.__z +1 #definition of drive is adding 1 grain to the first site in the model
        self.__h[0] = self.__z +1 #height of site_0
        
        

class grid:
    
    def __init__(self, L):
        self.__L = L
        self.__height = 3*L
        self.__initgrid = np.zeros(self.__height, L) #creates a 2d array with dimensions of height and length
   
        
        
        