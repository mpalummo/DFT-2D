# Relax the equilibrium cell and the atomic positions of the AB-BG
Enter in the AB directory

cd  DFT-2D/C-2L/AB
cd vc-relax/PBE+vdW

mpirun pw.x < c_2l_AB.vc-relax.in > c_2l_AB.vc-relax.out 

open the file c_2l_AB.vc-relax.out, look for CELL_PARAMETERS at the end of the file
multiply the alat value for the x component of the first vector of CELL_PARAMETERS 4.66447000*1.000195307 = 4.66538 . 
This is the new relaxed lattice parameter in xy-plane. Multiply 8.002109543*0.1675543188/8 = .16759830180868500000

Insert these numbers in the input c_2l.relax.in and run it to see the atoms
will not move
mpirun pw.x < c_2l_AB.relax.in > c_2l_AB.relax.out 
