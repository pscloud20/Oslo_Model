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

#%%

N=1000
L=16

test_1 = oslo(L, 0.5)
test_1.sim(N, h1_data = True)
h1 = test_1.h1()

print(len(h1))


plt.plot(np.arange(0,N, 1), h1)
plt.ylim(0,35)
plt.vlines(300,0,35)
mean  = np.mean(h1)
print(mean)

