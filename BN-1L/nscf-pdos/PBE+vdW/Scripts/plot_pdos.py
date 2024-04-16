#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

pdos_b1s = np.genfromtxt('./bn_1l_PBE_vdW_DOS60.dat.pdos_atm#1(B)_wfc#1(s)',comments="#")
pdos_b1p = np.genfromtxt('./bn_1l_PBE_vdW_DOS60.dat.pdos_atm#1(B)_wfc#2(p)',comments="#")
pdos_n1s = np.genfromtxt('./bn_1l_PBE_vdW_DOS60.dat.pdos_atm#2(N)_wfc#1(s)',comments="#")
pdos_n1p = np.genfromtxt('./bn_1l_PBE_vdW_DOS60.dat.pdos_atm#2(N)_wfc#2(p)',comments="#")

fig, axs = plt.subplots()
efermi= -1.8049
axs.set_ylabel('$ E(eV) $',fontsize=16)
axs.set_ylabel('$PDOS$',fontsize=16)
axs.set_title('graphene 1L 50x50x1 k-grid',fontsize=16)

axs.plot(pdos_b1s[:,0]-efermi,pdos_b1s[:,1]*10,linewidth=2,color='y',label='B s x10')
axs.plot(pdos_b1p[:,0]-efermi,pdos_b1p[:,1],linewidth=2,color='black',label='B p')
axs.plot(pdos_n1s[:,0]-efermi,pdos_n1s[:,1]*10,linewidth=1,color='cyan',label='N s x10')
axs.plot(pdos_n1p[:,0]-efermi,pdos_n1p[:,1],linewidth=3,color='m',label='N p')

axs.legend(loc="upper right")

axs.set_xlim(-5,5)
axs.set_ylim(0,0.8)

plt.savefig('pdos60kpt_bn_1l_PBE_vdW.png', format='png')
plt.show()
