#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

dos15 = np.genfromtxt('./graphene_PBE_vdW_DOS15.dat',comments="#")
dos20 = np.genfromtxt('./graphene_PBE_vdW_DOS20.dat',comments="#")
dos25 = np.genfromtxt('./graphene_PBE_vdW_DOS25.dat',comments="#")
dos30 = np.genfromtxt('./graphene_PBE_vdW_DOS30.dat',comments="#")
dos40 = np.genfromtxt('./graphene_PBE_vdW_DOS40.dat',comments="#")
dos50 = np.genfromtxt('./graphene_PBE_vdW_DOS50.dat',comments="#")
dos60 = np.genfromtxt('./graphene_PBE_vdW_DOS60.dat',comments="#")
fig, axs = plt.subplots()
efermi= -1.8049
axs.set_ylabel('$ E(eV) $',fontsize=16)
axs.set_ylabel('$DOS$',fontsize=16)
axs.set_title('graphene 1L',fontsize=16)

#axs.plot(dos15[:,0]-efermi,dos15[:,1],linewidth=2,color='g',label='kpt15')
#axs.plot(dos20[:,0]-efermi,dos20[:,1],linewidth=2,color='r',label='kpt20')
#axs.plot(dos25[:,0]-efermi,dos25[:,1],linewidth=2,color='orange',label='kpt25')
axs.plot(dos30[:,0]-efermi,dos30[:,1],linewidth=2,color='b',label='kpt30')
axs.plot(dos40[:,0]-efermi,dos40[:,1],linewidth=2,color='y',label='kpt40')
axs.plot(dos50[:,0]-efermi,dos50[:,1],linewidth=2,color='cyan',label='kpt50')
axs.plot(dos60[:,0]-efermi,dos60[:,1],linewidth=2,color='m',label='kpt60')

axs.legend(loc="upper right")

axs.set_xlim(-5,5)
axs.set_ylim(0,1.5)

plt.savefig('dos_vs_kpt_graphene_PBE_vdW.png', format='png')
plt.show()
