import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

with open('Bande_MoS2_2L_pbe_wsoc.dat.gnu', 'r') as file:
    lines = file.readlines()

colonna1 = []
colonna2 = []

sublists = []

efermi = 3.2402

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
    if  48 <= i <= 51 :
        plt.plot(sublist[0], sublist[1], color='red',alpha=0.7, lw=3)
    elif 52 <= i <= 55 :
        plt.plot(sublist[0], sublist[1], color='blue',alpha=0.7, lw=3)
    else:
        plt.plot(sublist[0], sublist[1], color='black', lw=2, alpha=1)


positions = [0,0.6349,1.,1.57]
labels = ['$\Gamma$','$K$','$M$','$\Gamma$']
plt.ylabel('E(eV)')
plt.xticks(positions, labels)

valori_y_visualizzati = [ -10, -5,-4,-1,0,1,2,4]
plt.yticks(valori_y_visualizzati)

plt.grid(1, linestyle='--', alpha=0.7)


xFermi=[0,1.7056]
yFermi=[0,0]

plt.plot(xFermi,yFermi,"--", color="black", label="$E_{F}$", lw=2)

plt.xlim(0,1.57)
plt.ylim(-4,4)

plt.title("$PBE+vdW-Bands-of-MoS2-2L-wSOC$")

plt.savefig('Bands_MoS2_2L_PBE_wSOC.png', format='png')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

