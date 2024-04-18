# Relax the equilibrium cell and the atomic positions of the MoS2-BULK using xc PBE+vdW 
Enter in the directory

cd  DFT-2D/MoS2-BULK/
cd vc-relax/PBE+vdW

cp ./Inputs/* .

mpirun pw.x < MoS2_BULK.vc-relax.in > MoS2_BULK.vc-relax.out 

open the MoS2_BULK.vc-relax.out , look for CELL_PARAMETERS and ATOMIC POSITIONS at the end of the file
They are used in the other input file MoS2_BULK.relax.in 

You can run it to see the atoms will not move now!
mpirun pw.x < MoS2_BULK.relax.in > MoS2_BULK.relax.out 

If you wish you can repeat similar calculations for PBE and LDA 
