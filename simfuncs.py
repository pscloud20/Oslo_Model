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
        self.__h = np.zeros(L) #same for heights as slopes use np.zeros over [] as it allows easier manipulation of elements and axes later on
        self.__threshold = []
        
    def drive(self): #define a drive function for when adding a grain 
        self.__z[0] = self.__z[0] +1 #definition of drive is adding 1 grain to the first site in the model
        self.__h[0] = self.__z[0] +1 #height of site_0 increases by 1
        
    def relax(self):
        
        
        
        
        for i in range(L):
            
            if i == 0: #behaviour of site 0 when relaxing
                self.__z[i] = self.__z[i] -2
                self.__z[i+1] = self.__z[i+1] + 1 #site 1 has a grain added since site 0 relaxes
            
            elif i !=0 or i != self.__L -1: #i.e. for i =2, ...
                self.__z[i] = self.__z[i]-2
                self.__z[i+1] = self.__z[i+1] +1
                self.__z[i-1] = self.__z[i-1] +1
            
            elif i == self.__L:
                self.__z[i] = self.__z[i]-1 #slope of L site -1 as it falls off grid
                self.__z[i-1] = self.__z[i-1] +1 #slope of L-1 site +1 as L site loses grain
                
                
                
                
            
        
        

class grid:
    
    def __init__(self, L):
        self.__L = L
        self.__height = 3*L
        self.__initgrid = np.zeros(self.__height, L) #creates a 2d array with dimensions of height and length
   
        
        
        