#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

etot_vs_ecut = np.genfromtxt('./Etot_vs_ecut_PBE.dat',comments="#")

fig, axs = plt.subplots(2)
#fig.suptitle('Convergence')
fig.subplots_adjust(bottom=0.2, left= 0.2,right=0.8, top=0.9,hspace=0.1,wspace=0.7)

#1
axs[0].set_ylabel('$E_{tot} (Ry)$',fontsize=16)
axs[1].set_ylabel('$E_{tot} (eV)$',fontsize=16)
axs[0].set_xticklabels([])

axs[0].plot(etot_vs_ecut[:,0],etot_vs_ecut[:,1],linewidth=2,color='r',label='graphene 1L')
axs[0].scatter(etot_vs_ecut[:,0],etot_vs_ecut[:,1],color='r')
axs[0].legend(loc="upper right")

axs[1].plot(etot_vs_ecut[:,0],etot_vs_ecut[:,1]*13.6057039763,linewidth=2,color='k',label='graphene 1L')
axs[1].scatter(etot_vs_ecut[:,0],etot_vs_ecut[:,1]*13.6057039763,color='k')
axs[1].legend(loc="upper right")
axs[1].set_xlabel('$E_{cut}(Ry)$',fontsize=16)
axs[0].set_xlim(40,100)
axs[1].set_xlim(40,100)
axs[0].set_ylim(-24.086,-24.)
axs[1].set_ylim(-327.27,-327.2)

plt.savefig('Etot_vs_ecut.png', format='png')
plt.show()
