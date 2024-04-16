# Relax the equilibrium cell and the atomic positions of the AB-BG
Enter in the AA directory

cd  DFT-2D/C-2L/AA
cd vc-relax/PBE+vdW

mpirun pw.x < c_2l_AA.vc-relax.in > c_2l_AA.vc-relax.out 

open the file c_2l_AA.vc-relax.out, look for CELL_PARAMETERS at the end of the file
You can find them inserted in c_2l_AB.relax.in and you can run this input seeying the atoms will not move this time

mpirun pw.x < c_2l_AB.relax.in > c_2l_AB.relax.out 
