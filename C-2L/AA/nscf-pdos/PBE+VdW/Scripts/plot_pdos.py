#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

pdos_c1s = np.genfromtxt('./C2L_AA_PBE_vdW_DOS.dat.pdos_atm#1(C)_wfc#1(s)',comments="#")
pdos_c1p = np.genfromtxt('./C2L_AA_PBE_vdW_DOS.dat.pdos_atm#1(C)_wfc#2(p)',comments="#")
pdos_c2s = np.genfromtxt('./C2L_AA_PBE_vdW_DOS.dat.pdos_atm#2(C)_wfc#1(s)',comments="#")
pdos_c2p = np.genfromtxt('./C2L_AA_PBE_vdW_DOS.dat.pdos_atm#1(C)_wfc#2(p)',comments="#")

pdos_c3s = np.genfromtxt('./C2L_AA_PBE_vdW_DOS.dat.pdos_atm#3(C)_wfc#1(s)',comments="#")
pdos_c3p = np.genfromtxt('./C2L_AA_PBE_vdW_DOS.dat.pdos_atm#3(C)_wfc#2(p)',comments="#")
pdos_c4s = np.genfromtxt('./C2L_AA_PBE_vdW_DOS.dat.pdos_atm#4(C)_wfc#1(s)',comments="#")
pdos_c4p = np.genfromtxt('./C2L_AA_PBE_vdW_DOS.dat.pdos_atm#4(C)_wfc#2(p)',comments="#")

fig, axs = plt.subplots()
efermi= -0.5954 
axs.set_ylabel('$ E(eV) $',fontsize=16)
axs.set_ylabel('$PDOS$',fontsize=16)
axs.set_title('AA-BG 60x60x1 k-grid',fontsize=16)

axs.plot(pdos_c1s[:,0]-efermi,pdos_c1s[:,1]*10,linewidth=2,color='y',label='C1 s x10')
axs.plot(pdos_c1p[:,0]-efermi,pdos_c1p[:,1]+0.01,linewidth=2,color='black',label='C1 pz')
axs.plot(pdos_c1p[:,0]-efermi,pdos_c1p[:,2]+0.02,linewidth=2,color='orange',label='C1 px')
axs.plot(pdos_c1p[:,0]-efermi,pdos_c1p[:,3]+0.03,linewidth=2,color='green',label='C1 py')
#axs.plot(pdos_c2s[:,0]-efermi,pdos_c2s[:,1]*10,linewidth=1,color='cyan',label='C2 s x10')
axs.plot(pdos_c2p[:,0]-efermi,pdos_c2p[:,1]+0.04,linewidth=3,color='m',label='C2 pz')
axs.plot(pdos_c3p[:,0]-efermi,pdos_c3p[:,1]+0.05,linewidth=3,color='brown',label='C3 pz')
axs.plot(pdos_c4p[:,0]-efermi,pdos_c4p[:,1]+0.06,linewidth=3,color='red',label='C4 pz')


axs.legend(loc="upper right")

axs.set_xlim(-5,5)
axs.set_ylim(0,0.4)

plt.savefig('C2L_AA_PBE_vdW_DOS.dat.pdos_tot', format='png')
plt.show()
