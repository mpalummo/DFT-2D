cd AB/bands/PBE+vdW

Copy the input files and script to run and plot  from the two directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file

run_bands.sh  close and run

./run_bands.sh

At the end you should have c_2l_AB.scf.out c_2l_AB.bands.out bands.out 
Open and check everythin is ok

Also 3 files Band* should be there. 
You can use the the script python plot_bands.py to plot them

python plot_bands.py 

At the end you should have a file Bande_AB-BG_vdW.png in a png format
# 
