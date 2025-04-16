#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

pot1 = np.genfromtxt('./avg.dat_18.539999999999999',comments="#")
pot2 = np.genfromtxt('./avg.dat_23.174999999999997',comments="#")
pot3 = np.genfromtxt('./avg.dat_27.809999999999999',comments="#")
pot4 = np.genfromtxt('./avg.dat_32.445',comments="#")
pot5 = np.genfromtxt('./avg.dat_37.079999999999998',comments="#")

fig, axs = plt.subplots()
fig.suptitle('Convergence with vacuum')
fig.subplots_adjust(bottom=0.2, left= 0.2,right=0.8, top=0.9,hspace=0.1,wspace=0.7)

#1
axs.set_ylabel('$[V_{e-I}+V_{H}] (Ry)$',fontsize=16)
axs.set_xlabel('cell size (au)',fontsize=16)

axs.plot(pot1[:,0],pot1[:,1],linewidth=2,color='r',label='c/a=4')
axs.plot(pot2[:,0],pot2[:,1],linewidth=2,color='m',label='c/a=5')
axs.plot(pot3[:,0],pot3[:,1],linewidth=2,color='b',label='c/a=6')
axs.plot(pot4[:,0],pot4[:,1],linewidth=2,color='g',label='c/a=7')
axs.plot(pot5[:,0],pot5[:,1],linewidth=2,color='y',label='c/a=8')
axs.legend(loc="upper right")

axs.set_xlim(0,32)
axs.set_ylim(0.0,0.3)

plt.savefig('Avg_pot.png', format='png')
plt.show()
