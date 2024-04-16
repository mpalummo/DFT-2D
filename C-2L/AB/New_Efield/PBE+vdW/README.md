#
cd  AB/New_Efield/PBE+vdW

Copy the input files and Scripts to run and tp plot  from the two sub-directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file

run_bands.sh,  close it  and run doing:

./run_bands.sh

At the end you should have C-2L-EF-AB.scf.out C-2L-EF-AB.bands.out C-2L-EF-AB.bands.pp.out 

Open them and check everything is ok

There should be also other 3 files Band* 
You can use the python script plot_bands.py to plot the B*gnu file.

python plot_bands.py 

At the end you should have a file Bande_AB-BG_vdW.png in a png format to plot.
Open the three output files and check that everything is ok

3 files Band* should be there. 
You can use the the script plot_bands.py to plot them

python plot_bands.py 

At the end you should have a file Bande-2-C2L_AB_Efield_PBE.png that is a png format
# 
