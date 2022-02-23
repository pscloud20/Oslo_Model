# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:49:27 2022

@author: PSClo
"""

import simfuncs  

#%%
L=10
initgrid = np.zeros((3*L, L))
anim_matrix = initgrid

ncolors = matplotlib.colors.ListedColormap(['white', 'black'])
boundaries = [0,0,1,1]
norm = matplotlib.colors.BoundaryNorm(boundaries, ncolors.N)
        
plt.pcolormesh(anim_matrix, norm = norm, cmap = ncolors)