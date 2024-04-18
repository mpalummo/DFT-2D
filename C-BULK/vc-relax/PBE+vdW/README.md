# Relax the equilibrium cell and the atomic positions of the C-BULK using xc PBE+vdW 
Enter in the directory

cd  DFT-2D/C-BULK/
cd vc-relax/PBE+vdW

cp ./Inputs/* .
mpirun pw.x < c_bulkAB.vcrelax.in > c_bulkAB.vcrelax.out

open the c_bulkAB.vcrelax.out, look for CELL_PARAMETERS and ATOMIC POSITIONS at the end of the file
They are used in the other input file  c_bulkAB.relax.in

You can run it to see the atoms will not move now!
mpirun pw.x < c_bulkAB.relax.in > c_bulkAB.relax.out

If you wish you can repeat similar calculations for PBE and LDA 
