import matplotlib.pyplot as plt
import numpy as np

colonna1 = []
colonnasno1=[]
colonnaso1=[]
colonna2 = []
colonnasno2=[]
colonnaso2=[]
colonna3 = []

E_Fermi=-1.6656
x_Fermi=[0,0]
y_Fermi=[0,2.5]


with open('graphene_PBE_pdos.dat.pdos_tot', 'r') as file:
    righe = file.readlines()

    for riga in righe[1:]:
        valori = riga.split()
        colonna1.append(float(valori[0])-E_Fermi)
        colonna2.append(float(valori[1]))
        colonna3.append(float(valori[2]))
        if float(valori[0])-E_Fermi <= 0:
            colonnasno1.append((float(valori[0]))-E_Fermi)
            colonnasno2.append((float(valori[1])))
        else:
            colonnaso1.append((float(valori[0]))-E_Fermi)
            colonnaso2.append((float(valori[1])))


fig = plt.figure(figsize=(8, 6), facecolor='white')

plt.title("$ \ D.O.S. \ Graphene PBE$")

plt.xlim(-5,5)
plt.ylim(0,2.5)

plt.grid(1, linestyle='--', alpha=0.7)

plt.xlabel("$E \  [eV]$", fontsize=12)
plt.ylabel("$DOS$", fontsize=12)

valori_y_visualizzati = [ 0,0.5,1.,1.5,2. ]
plt.yticks(valori_y_visualizzati)


plt.plot(colonna1,colonna2, color="black", linewidth=2, label="$D.O.S$")
plt.legend()

plt.plot(colonnasno1,colonnasno2, color="black", linewidth=2)

plt.fill_between(colonnasno1, colonnasno2, color='red', alpha=0.5, label='$Stati\ Occupati$')
plt.legend()

plt.plot(colonnaso1,colonnaso2, color="black", linewidth=2)

plt.fill_between(colonnaso1, colonnaso2, color='blue', alpha=0.5, label='$Stati\ non \ Occupati$')
plt.legend()

plt.plot(x_Fermi,y_Fermi, "--", color="black", label="$Energia \ di \ Fermi$", lw=2)
plt.legend()

plt.show()

