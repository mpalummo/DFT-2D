#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

dos20 = np.genfromtxt('./epsilon21.dat',comments="#")
dos40 = np.genfromtxt('./epsilon24.dat',comments="#")
dos50 = np.genfromtxt('./epsilon27.dat',comments="#")
fig, axs = plt.subplots()
efermi= -0.5713 
axs.set_ylabel('$ E(eV) $',fontsize=16)
axs.set_ylabel('epsilon2',fontsize=16)
axs.set_title('AB-BG-PBE+vdW',fontsize=16)

axs.plot(dos20[:,0]-efermi,dos20[:,1],linewidth=2,color='r',label='kpt21')
axs.plot(dos40[:,0]-efermi,dos40[:,1],linewidth=2,color='y',label='kpt24')
axs.plot(dos50[:,0]-efermi,dos50[:,1],linewidth=2,color='cyan',label='kpt27')

axs.legend(loc="upper right")

axs.set_xlim(0,20)
axs.set_ylim(0,40)

plt.savefig('eps2_kpt_PBE_vdW.png', format='png')
plt.show()
