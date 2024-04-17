# Relax the equilibrium cell and the atomic positions of the AB-BG
Enter in the AB1 directory

cd  DFT-2D/BN-2L/AB1/vc-relax/PBE+vdW

cp ./Inputs/* .

mpirun pw.x < bn_2l.vc-relax.in > bn_2l.vc-relax.out 

then from the bn_2l.vc-relax.out you can extract the equilibrium cell and atomic positions which
are substituted in another input already prepared so you can run

mpirun pw.x < bn_2l.relax.in > bn_2l.relax.out

You should see that actually the forces are almost zero and the atoms do not move anymore
 
Use the relaxed cell  and atomic positions in the other directories where scf and nscf calculations
and postprocessing are performed.

If you wish you can find the equilibrium structure using a similar procedure for PBE and LDA cases
