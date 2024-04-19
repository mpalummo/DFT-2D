#
cd C-BN-2L/scf-bands/PBW+vdW

Copy the input files and Scripts files to run and to plot the Bandstructure

cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file
run_bands.sh,  close it  and run doing:

./run_bands.sh

At the end you should have  cbn_2l_AB.scf.out, cbn_2l_AB.bands.out, bands.out 

Open them and check that everything is ok

There should be also other 3 files Band* 
You can use the python script plot_bands.py to plot the B*gnu file

python plot_bands.py 

At the end you should have a file Bands_CBN_2L_AB_PBE-vdW.png in a png format 

you can repeat the plotting zooming around E_F and see how a gap is open for graphene has expected from the theoretical TB model
If you wish you can repeat the same calculations for the LDA and PBE relaxed structures and compare them 
