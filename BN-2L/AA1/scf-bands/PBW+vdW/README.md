#
cd BN-2L/AA1/scf-bands/PBE+vdW

Copy the input files and Scripts files to run and to plot the Bandstructure

cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file
run_bands.sh,  close it  and run doing:

./run_bands.sh

At the end you should have bn_2l.scf.out, bn_2l.bands.out, bands.out 

Open them and check everything is ok

There should be also other 3 files Band* 
You can use the python script plot_bands.py to plot the B*gnu file

python plot_bands.py 

At the end you should have a file Bands_BN_2L_AA1_PBE-vdW.png in a png format 

If you wish you can repeat the same calculations for the LDA and PBE relaxed structures and compare them 
