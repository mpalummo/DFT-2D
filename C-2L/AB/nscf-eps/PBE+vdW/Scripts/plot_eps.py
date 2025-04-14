#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

epsi = np.genfromtxt('epsi_C2L_AB_PBE_vdW.dat',comments="#")
epsr = np.genfromtxt('epsr_C2L_AB_PBE_vdW.dat',comments="#")
fig, axs = plt.subplots()
efermi= 0.0 
axs.set_ylabel('$ E(eV) $',fontsize=16)
axs.set_ylabel('epsilon',fontsize=16)
axs.set_title('AB-C2L-PBE+vdW',fontsize=16)

axs.plot(epsi[:,0]-efermi,epsi[:,1],linewidth=2,color='r',label='Im')
axs.plot(epsr[:,0]-efermi,epsr[:,1],linewidth=2,color='b',label='Real')

axs.legend(loc="upper right")

axs.set_xlim(0,20)
axs.set_ylim(-10,40)

plt.savefig('eps2_kpt_PBE_vdW.png', format='png')
plt.show()
