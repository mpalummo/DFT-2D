
import matplotlib.pyplot as plt
import numpy as np



with open('../../bands/PBE+VdW/Ref/Bande_C2L_AB_PBE_vdW.dat.gnu', 'r') as file:
    lines = file.readlines()

colonna1_bs = []
colonna2_bs = []

sublists_bs = []
efermi1 = -0.5713
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

colonna1 = []
colonnasno1=[]
colonnaso1=[]
colonna2 = []
colonnasno2=[]
colonnaso2=[]
colonna3 = []

x_Fermi=[0,0]
y_Fermi=[0,2.5]

efermi2 = -0.5954

with open('C2L_AB_PBE_vdW_DOS.dat', 'r') as file:
    righe = file.readlines()
    for riga in righe[1:]:
        valori = riga.split()
        colonna1.append(float(valori[0])-efermi2)
        colonna2.append(float(valori[1]))
        colonna3.append(float(valori[2]))
        if float(valori[0])-efermi2 <= 0:
            colonnasno1.append((float(valori[0]))-efermi2)
            colonnasno2.append((float(valori[1])))
        else:
            colonnaso1.append((float(valori[0]))-efermi2)
            colonnaso2.append((float(valori[1])))


larghezza_figura = 8 
altezza_figura = 6

larghezza_relativa_subplots = [2.5,1.5]

fig, axs = plt.subplots(1, 2, sharey=True, figsize=(larghezza_figura, altezza_figura), gridspec_kw={'width_ratios': larghezza_relativa_subplots})
plt.subplots_adjust(wspace=0.025)  

for i, sublist in enumerate(sublists_bs):
    if i<=7:
        axs[0].plot(sublist[0], sublist[1], color='red', lw=2, alpha=1)
    else:
        axs[0].plot(sublist[0], sublist[1], color='blue', lw=2, alpha=1)

positions = [0,0.6349,1.,1.57]
labels = ['$\Gamma$','$K$','$M$','$\Gamma$']

axs[0].set_xticks(positions)
axs[0].set_xticklabels(labels)

valori_y_visualizzati = [-10,-5,-4,-1,0,1,2,4]
axs[1].set_yticks(valori_y_visualizzati)

axs[0].grid(1, linestyle='--', alpha=0.7)
axs[1].grid(1, linestyle='--', alpha=0.7)

axs[0].set_title("$Bands$")
axs[1].set_title("$D.O.S. \ of \ AB\ BG $")


axs[0].set_xlim(0,1.57)
axs[0].set_ylim(-6,6) 
axs[1].set_xlim(0,1.5)
axs[1].set_ylim(-6,6)
axs[0].plot(xFermi,yFermi,"--", color="black", label="$E_F$", lw=2)
axs[1].plot(y_Fermi,x_Fermi,"--", color="black", label="$E_F$", lw=2)
axs[1].plot(colonnasno2, colonnasno1, color="red", lw=2, label="$Occupied\ states$")
axs[1].plot(colonnaso2, colonnaso1, color="blue", lw=2, label="$Unoccupied\ states$")
axs[1].legend(loc='lower right')

plt.savefig('bands-dos_AB-BG_PBE_vdW.png', format='png')
plt.show()
