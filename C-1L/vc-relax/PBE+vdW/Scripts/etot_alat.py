#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

etot_vs_ecut = np.genfromtxt('./Etot_vs_alat_pbe-vdW.dat',comments="#")
etot_vs_ecut1 = np.genfromtxt('../PBE/Ref/Etot_vs_alat_pbe.dat',comments="#")

fig, axs = plt.subplots()
#fig.suptitle('Convergence')

axs.set_ylabel('$alat (bohr) $',fontsize=16)
axs.set_ylabel('$E_{tot} (Ry)$',fontsize=16)
axs.set_title('graphene 1L',fontsize=16)

axs.plot(etot_vs_ecut[:,0],etot_vs_ecut[:,1],linewidth=2,color='g',label='PBE+vdW')
axs.scatter(etot_vs_ecut[:,0],etot_vs_ecut[:,1],color='g')
axs.plot(etot_vs_ecut1[:,0],etot_vs_ecut1[:,1]+24.09516737-24.12355371,linewidth=2,color='r',label='PBE')
axs.scatter(etot_vs_ecut1[:,0],etot_vs_ecut1[:,1]+24.09516737-24.12355371,color='r')

axs.legend(loc="upper right")

axs.set_xlim(4.55,4.75)
axs.set_ylim(-24.125,-24.11)

plt.savefig('Etot_vs_alat_pbe-vdW.png', format='png')
plt.show()
