#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

dos20 = np.genfromtxt('./C2L_AB_PBE_vdW_DOS20.dat',comments="#")
dos40 = np.genfromtxt('./C2L_AB_PBE_vdW_DOS40.dat',comments="#")
dos50 = np.genfromtxt('./C2L_AB_PBE_vdW_DOS50.dat',comments="#")
dos60 = np.genfromtxt('./C2L_AB_PBE_vdW_DOS60.dat',comments="#")
fig, axs = plt.subplots()
efermi= -0.5713 
axs.set_ylabel('$ E(eV) $',fontsize=16)
axs.set_ylabel('$DOS$',fontsize=16)
axs.set_title('AB-BG-PBE+vdW',fontsize=16)

axs.plot(dos20[:,0]-efermi,dos20[:,1],linewidth=2,color='r',label='kpt20')
axs.plot(dos40[:,0]-efermi,dos40[:,1],linewidth=2,color='y',label='kpt40')
axs.plot(dos50[:,0]-efermi,dos50[:,1],linewidth=2,color='cyan',label='kpt50')
axs.plot(dos60[:,0]-efermi,dos60[:,1],linewidth=2,color='m',label='kpt60')

axs.legend(loc="upper right")

axs.set_xlim(-5,5)
axs.set_ylim(0,1.5)

plt.savefig('dos_vs_kpt_AB-BG_PBE_vdW.png', format='png')
plt.show()
