#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

pdos_c1p = np.genfromtxt('./CBN2L_AB_PBE_vdW_DOS.dat.pdos_atm#1(C)_wfc#2(p)',comments="#")
pdos_c3p = np.genfromtxt('./CBN2L_AB_PBE_vdW_DOS.dat.pdos_atm#3(C)_wfc#2(p)',comments="#")
pdos_b2p = np.genfromtxt('./CBN2L_AB_PBE_vdW_DOS.dat.pdos_atm#2(B)_wfc#2(p)',comments="#")
pdos_n4p = np.genfromtxt('./CBN2L_AB_PBE_vdW_DOS.dat.pdos_atm#4(N)_wfc#2(p)',comments="#")

fig, axs = plt.subplots()
efermi=  -0.8916
axs.set_ylabel('$ E(eV) $',fontsize=16)
axs.set_ylabel('$PDOS$',fontsize=16)
axs.set_title('CBN-2L 60x60x1 k-grid',fontsize=16)

axs.plot(pdos_c1p[:,0]-efermi,pdos_c1p[:,1]+0.01,linewidth=2,color='black',label='C1 pz')
axs.plot(pdos_c3p[:,0]-efermi,pdos_c3p[:,2]+0.02,linewidth=2,color='orange',label='C2 pz')
axs.plot(pdos_b2p[:,0]-efermi,pdos_b2p[:,3]+0.03,linewidth=2,color='green',label='B pz')
axs.plot(pdos_n4p[:,0]-efermi,pdos_n4p[:,1]+0.04,linewidth=1,color='cyan',label='N pz')

axs.set_xlabel ('E(eV)')

axs.legend(loc="upper right")

axs.set_xlim(-5,5)
axs.set_ylim(0,0.4)

plt.savefig('CBN2L_AB_PBE_vdW_DOS.dat.pdos_tot', format='png')
plt.show()
