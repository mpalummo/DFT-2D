#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

etot_vs_ecut = np.genfromtxt('./Etot_vs_alat.dat',comments="#")

fig, axs = plt.subplots()
#fig.suptitle('Convergence')

axs.set_ylabel('$alat (bohr) $',fontsize=16)
axs.set_ylabel('$E_{tot} (Ry)$',fontsize=16)

axs.plot(etot_vs_ecut[:,0],etot_vs_ecut[:,1],linewidth=2,color='r',label='graphene 1L')
axs.scatter(etot_vs_ecut[:,0],etot_vs_ecut[:,1],color='r')
axs.legend(loc="upper right")

axs.set_xlim(4.5,4.7)
axs.set_ylim(-24.123,-24.11)

plt.savefig('Etot_vs_alat.png', format='png')
plt.show()
