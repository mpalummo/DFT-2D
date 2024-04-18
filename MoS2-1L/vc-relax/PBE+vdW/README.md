# Relax the equilibrium cell and the atomic positions of the MoS2-1L using xc PBE+vdW 
Enter in the directory

cd  DFT-2D/MoS2-1L/
cd vc-relax/PBE+vdW

mpirun pw.x < MoS2_1L.vc-relax.in > MoS2_1L.vc-relax.out 

open the MoS2_1L.vc-relax.out , look for CELL_PARAMETERS and ATOMIC POSITIONS at the end of the file
They are used in the other input file MoS2_1L.relax.in 

You can run it to see the atoms will not move now!
mpirun pw.x < MoS2_1L.relax.in > MoS2_1L.relax.out 

the same structure is used in the other directories to perform scf and bands calculations

If you wish you can repeat similar calculations for PBE and LDA 
