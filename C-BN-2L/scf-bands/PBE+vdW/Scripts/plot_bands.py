import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

with open('Bande_CBN2L_AB_PBE_vdW.dat.gnu', 'r') as file:
    lines = file.readlines()

colonna1 = []
colonna2 = []

sublists = []

efermi = -0.8892

for line in lines:
    if line.strip(): 
        values = line.split()
        colonna1.append(float(values[0]))
        colonna2.append(float(values[1]) -efermi  ) 
    else:
        sublists.append((colonna1, colonna2))
        colonna1= []
        colonna2 = []
        
for i, sublist in enumerate(sublists):
    if i == 7:
        plt.plot(sublist[0], sublist[1], color='red',alpha=0.7, lw=3, label="$VBM$")
    elif i == 8:
        plt.plot(sublist[0], sublist[1], color='blue',alpha=0.7, lw=3, label="$CBM$")
    else:
        plt.plot(sublist[0], sublist[1], color='black', lw=2, alpha=1)


positions = [0,0.6667,1.,1.5773]
labels = ['$\Gamma$','$K$','$M$','$\Gamma$']
plt.xticks(positions, labels)

valori_y_visualizzati = [ -10, -5,-4,-1,0,1,2,4]
plt.yticks(valori_y_visualizzati)

plt.grid(1, linestyle='--', alpha=0.7)


xFermi=[0,1.5773]
yFermi=[0,0]

plt.plot(xFermi,yFermi,"--", color="black", label="$E_{F}$", lw=2)

#plt.xlim(0.61,0.7)
#plt.ylim(-1,1)

plt.xlim(0.,1.5773)
plt.ylim(-10,10)

plt.title("$PBE+vdW-Bands-of-2L-CBN-AB$")

plt.savefig('Bands_CBN_2L_AB_PBE-vdW.png', format='png')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

