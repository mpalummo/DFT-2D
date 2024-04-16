# Relax the equilibrium cell and the atomic positions of the AB-BG
Enter in the AA directory

cd  DFT-2D/BN-2L/AA/vc-relax/PBE+vdW

cp ./Inputs/* .

mpirun pw.x < bn_2l.vc-relax.in > bn_2l.vc-relax.out 

Use the relaxed geometry in the other scf and nscf calculations

If you wish you can find the equilibrium structure for PBE and LDA cases
