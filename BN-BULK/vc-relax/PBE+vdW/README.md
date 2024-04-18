# Relax the equilibrium cell and the atomic positions of the BN bulk 
Enter in the directory

cd  DFT-2D/BN-BULK
cd vc-relax/PBE+vdW


cp ./Inputs/* .
cp ./Scripts/* .

open the file run_vc-relax.sh and the 3 input files where a different vdW functional is used

close the files and run the script

./run_vc-relax.sh


At the end you will produce the 3 outputs and  compare the optimized lattice parameters with the experimental data 
to see which is the best to be used

If you wish you can repeat a vc-relax calculation for PBE and LDA and compare the lattice parameteres how they compare among them
and with experimental data

