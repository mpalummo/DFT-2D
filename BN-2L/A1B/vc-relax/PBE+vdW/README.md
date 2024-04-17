# Relax the equilibrium cell and the atomic positions of the AB-BG
Enter in the A1B directory

cd  DFT-2D/BN-2L/A1B/vc-relax/PBE+vdW

cp ./Inputs/* .

mpirun pw.x < bn_2l.vc-relax.in > bn_2l.vc-relax.out 

The relaxed cell and atomic position at the end of the file have introduced in the other input bn_2l.relax.in 
you can run it and check the atoms will not move since they are already at the equilibrium

mpirun pw.x < bn_2l.relax.in > bn_2l.relax.out 

The equilibrium structure is used in the inputs files of the other directories where scf and nscf or bands or post-prosessing are only done

If you wish you can find the equilibrium structure for PBE and LDA cases
