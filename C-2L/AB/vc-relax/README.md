# Relax the equilibrium cell and the atomic positions of the AB-BG
Enter in the AB directory

cd  DFT-2D/C-2L/AB
cd vc-relax/PBE+vdW

mpirun pw.x < c_2l_AB.vc-relax.in > c_2l_AB.vc-relax.out 

open the file c_2l_AB.vc-relax.out, look for CELL_PARAMETERS and ATOMIC POSITIONS at the end of the file
They are used in the other input file c_2l_AB.relax.in 

You can run it to see the atoms will not move now!
mpirun pw.x < c_2l_AB.relax.in > c_2l_AB.relax.out 

If you wish you can repeat similar calculations for PBE and LDA 
