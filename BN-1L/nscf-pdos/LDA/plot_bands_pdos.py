
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


with open('../../bands/LDA/Ref/Bande_hBN_1l_LDA.dat.gnu', 'r') as file:
    lines = file.readlines()

colonna1_bs = []
colonna2_bs = []

sublists_bs = []

efermi1 = -1.6804 
efermi2 =  0.3

for line in lines:
    if line.strip():  
        values = line.split()
        colonna1_bs.append(float(values[0]))
        colonna2_bs.append(float(values[1]) -efermi1)  
    else:
        sublists_bs.append((colonna1_bs, colonna2_bs))
        colonna1_bs= []
        colonna2_bs = []
        
xFermi=[0,1.8]
yFermi=[0,0]


x_Fermi=[0,0]
y_Fermi=[0,2.5]


dos_B_p = np.genfromtxt('hBN_1l_LDA_pdos.dat.pdos_atm#1(B)_wfc#2(p)',comments="#")
dos_N_p = np.genfromtxt('hBN_1l_LDA_pdos.dat.pdos_atm#2(N)_wfc#2(p)',comments="#")


larghezza_figura = 8 
altezza_figura = 6

larghezza_relativa_subplots = [2.5,1.5]

fig, axs = plt.subplots(1, 2, sharey=True, figsize=(larghezza_figura, altezza_figura), gridspec_kw={'width_ratios': larghezza_relativa_subplots})
plt.subplots_adjust(wspace=0.025)  

for i, sublist in enumerate(sublists_bs):
    if i<=3:
        axs[0].plot(sublist[0], sublist[1], color='red', lw=2, alpha=1)
    else:
        axs[0].plot(sublist[0], sublist[1], color='black', lw=2, alpha=1)

positions = [0,0.6349,1.,1.57]
labels = ['$\Gamma$','$K$','$M$','$\Gamma$']

axs[0].set_xticks(positions)
axs[0].set_xticklabels(labels)
axs[0].set_ylabel('E(eV)')
valori_y_visualizzati = [-10,-5,-4,-1,0,1,2,4]
axs[1].set_yticks(valori_y_visualizzati)

axs[0].grid(1, linestyle='--', alpha=0.7)
axs[1].grid(1, linestyle='--', alpha=0.7)

axs[0].set_title("$Bands$")
axs[1].set_title("$P.D.O.S. \ of \ BN\ 1L $")


axs[0].set_xlim(0,1.57)
axs[0].set_ylim(-10,10) 
axs[1].set_xlim(0,0.5)
axs[1].set_ylim(-10,10)
axs[0].plot(xFermi,yFermi,"--", color="black", label="$E_F$", lw=2)
axs[1].plot(y_Fermi,x_Fermi,"--", color="black", label="$E_F$", lw=2)
axs[1].plot(dos_B_p[:,1], dos_N_p[:,0]-efermi2, color="orange", lw=2, label="$p_z B  $")
axs[1].plot(dos_N_p[:,1]+0.01, dos_N_p[:,0]-efermi2, color="green", lw=2, label="$p_z N  $")
axs[1].legend(loc='upper right')


plt.savefig('Bande_pdos60kpt_hBN_1L_LDA.png', format='png')
plt.show()
