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
import random
from matplotlib.colors import LogNorm
import matplotlib




#%%

def randomprob(probability):
    seed = random.randint(0,10000)
    rg = default_rng(seed)
    y = rg.random()
    if y < probability:
        return 1
    if y >= probability:
        return 2

#%%

#defining site 1 in mathematical oslo model as site 0

class oslo:
    
    def __init__(self, L, prob): #calling class objects length of model and probability
        self.L = L 
        self.p = prob
        self.z = np.zeros(L) #initialise array length L that contains slopes at each site (initially 0 will add values later)
        self.h = np.zeros(L) #same for heights as slopes use np.zeros over [] as it allows easier manipulation of elements and axes later on
        self.thresholdz = []
        self.sites = []
        self.s_size = []
        
    def s_size(self):
        return s_size
        
    def drive(self): #define a drive function for adding grain to site_0 
        self.z[0] = self.z[0] +1 #definition of drive is adding 1 grain to the first site in the model
        self.h[0] = self.z[0] +1 #height of site_0 increases by 1
        
    def relax(self):
        sites_relaxed = []
        sites_totalrelax = False 
        self.s = 0 #avalanche size
        
# =============================================================================
#         while len(sites_relaxed) > 0:
#             sites_relaxed = []
#             
#             for i in range(self.L):
#             if self.z[i] > self.thresholdz[i]:
#                 #sites_relaxed.append(i)
#                     
#             for i in sites_relaxed:
#                 self.s = self.s +1
#                 self.h[i] = self.h[i]+1
# =============================================================================
        
#When system is not relaxed ie when slope[i] is larger than threshold, the total system is False
        for i in range(self.L):
            if self.z[i] > self.thresholdz[i]:
                #sites_relaxed.append(i)
                sites_totalrelax = False
                break #ensures inner loop stops executing
            else:
                sites_totalrelax = True
                
        while sites_totalrelax is False: 
            if self.z[i] > self.thresholdz[i]:
            
# =============================================================================
#                 if i != self.L -1:
#                     self.h[i+1] = self.h[i+1] +1
# =============================================================================
                    
                if i == 0: #behaviour of site 0 when relaxing
                    self.z[i] = self.z[i] -2
                    self.z[i+1] = self.z[i+1] + 1 #site 1 has a grain added since site 0 relaxes
                
                elif i !=0 or i != self.__L-1: #i.e. for i =2, ...
                    self.z[i] = self.z[i]-2
                    self.z[i+1] = self.z[i+1] +1
                    self.z[i-1] = self.z[i-1] +1
            
                elif i == self.L-1:
                    self.z[i] = self.z[i]-1 #slope of L site -1 as it falls off grid
                    self.z[i-1] = self.z[i-1] +1 #slope of L-1 site +1 as L site loses grain
                
                self.thresholdz[i] = randomprob(self.p)
                
                
    def animate(self):
        grid = grid(self)
        for i in range(self.L):
            for j in range(self.heights[i]):
                grid.addgrain(i+1)
    
    def h(self):
        return self.h
    def h_1(self):
        return self.h_data
    def steadystate(self):
        for i in range(len(self.h_data)):
            if self.h_data[i] > np.max(self.h_1[len(self.h_data())-100:])
    def mean_h(self):
        return np.mean(self.h_data[self.steadystate:])
    
    
                
            
            
                
                
                
            
#create a class that sets up animation for grid
class grid:
    
    def __init__(self, L):
        self.L = L
        self.gheight = 3*L
        self.initgrid = np.zeros((3*L, L)) #creates a 2d array with dimensions of height and length
        
    def addgrain(self, g):
        for i in range(self.gridh):
            if self.initgrid[i][i-1] ==0:
                self.initgrid[i][i-1] =1
            
    def minusgrain(self,g):
        for i in range(self.gridh):
            if self.initgrid[i][i-1] ==1:
                self.initgrid[i][i-1] =0
        
        
    def showanimation(self):
        
        params = {
            'font.family' : 'serif',
            'font.size': 13.5,
            'figure.figsize':  [8.8, 8.8/1.618],
            'axes.grid': True,
   
        }

        plt.rcParams.update(params)
        
        fig = plt.figure()
        anim_matrix = self.initgrid
        ncolors = matplotlib.ListedColormap(['white', 'black'])
        boundaries = [0,0,1,1]
        norm = matplotlib.colors.BoundaryNorm(boundaries, ncolors.N)
        
        plt.pcolormesh(anim_matrix, norm = norm, cmap = ncolors)
        
        plt.xticks(np.arange(0,self.L, 1))
        plt.yticks(np.arange(0,3*self.L, 1))
        
        plt.grid()
        plt.show()
        
        
        
        
        
            
#%%
L =10
initgrid = np.zeros((3*L, L))
cmap = matplotlib.colors.ListedColormap(['white', 'black'])
bounds = [0, 0, 1, 1]
norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)  
plt.pcolormesh(initgrid, edgecolors=None, linewidth=1, norm=norm, cmap=cmap)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        