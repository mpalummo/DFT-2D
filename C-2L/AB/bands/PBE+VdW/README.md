#
cd AB/bands/PBE+vdW

Copy the input files and Scripts files to run and to plot data 
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file
run_bands.sh,  close it  and run doing:

./run_bands.sh

At the end you should have c_2l_AB.scf.out, c_2l_AB.bands.out, bands.out 
Open them and check everything is ok

There should be also other 3 files Band* 
You can use the python script plot_bands.py to plot them.

python plot_bands.py 

At the end you should have a file Bande_AB-BG_PBE_vdW.png in a png format to plot.
# 
