import matplotlib.pyplot as plt
import numpy as np

colonna1 = []
colonna2 = []


with open('Etot_vs_ecut.dat', 'r') as file:
    righe = file.readlines()

    for riga in righe[1:]:
        valori = riga.split()
        colonna1.append(float(valori[0]))
        colonna2.append(float(valori[1]))

plt.title("$Convergenza\ E_{cut}$", fontsize=15)

plt.plot(colonna1,colonna2, color="black", lw=2)

plt.plot(colonna1,colonna2, ".", color="black", lw=2)

# Add horizontal lines at specific y-values
y1 = -24.0820185  # +10 meV 
y2 = -24.0754037  # +100 meV 
plt.axhline(y=y1, color='red', linestyle='--', linewidth=1.5, label=f"+10meV")
plt.axhline(y=y2, color='blue', linestyle='--', linewidth=1.5, label=f"+100meV")

plt.xlabel("$Energia_{cut} \ [Ry]$")

plt.ylabel("$Energia \ [Ry]$")

plt.grid(1, linestyle='--', alpha=0.7)


plt.show()
