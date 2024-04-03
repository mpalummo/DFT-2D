#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

pdos_c1s = np.genfromtxt('./graphene_PBE_vdW_DOS50.dat.pdos_atm#1(C)_wfc#1(s)',comments="#")
pdos_c1p = np.genfromtxt('./graphene_PBE_vdW_DOS50.dat.pdos_atm#1(C)_wfc#2(p)',comments="#")
pdos_c2s = np.genfromtxt('./graphene_PBE_vdW_DOS50.dat.pdos_atm#2(C)_wfc#1(s)',comments="#")
pdos_c2p = np.genfromtxt('./graphene_PBE_vdW_DOS50.dat.pdos_atm#2(C)_wfc#2(p)',comments="#")
fig, axs = plt.subplots()
efermi= -1.8049
axs.set_ylabel('$ E(eV) $',fontsize=16)
axs.set_ylabel('$PDOS$',fontsize=16)
axs.set_title('graphene 1L 50x50x1 k-grid',fontsize=16)

axs.plot(pdos_c1s[:,0]-efermi,pdos_c1s[:,1]*10,linewidth=2,color='y',label='C1 s x10')
axs.plot(pdos_c1p[:,0]-efermi,pdos_c1p[:,1],linewidth=2,color='black',label='C1 p')
axs.plot(pdos_c2s[:,0]-efermi,pdos_c2s[:,1]*10,linewidth=1,color='cyan',label='C2 s x10')
axs.plot(pdos_c2p[:,0]-efermi,pdos_c2p[:,1],linewidth=3,color='m',label='C2 p')

axs.legend(loc="upper right")

axs.set_xlim(-5,5)
axs.set_ylim(0,0.8)

plt.savefig('pdos50kpt_graphene_PBE_vdW.png', format='png')
plt.show()
