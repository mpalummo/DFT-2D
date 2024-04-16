#
cd AB/nscf-dos-stm/PBE+vdW

Copy the input files and script to run and plot  from the two directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script files
run_nscf-dos_k.sh and  run_nscf-dos_stm.sh. 

The first script performs one scf calculation and several nscf and dos calculations using different k-points grids to check convergence over k-points. 

./run_nscf-dos_k.sh 

The second script runs one scf calculation, one nscf calculation with the selected k-grid at convergence and then again a dos calculation and also an STM image as post-processing

At the end you should have c_2l_AB.scf.out, c_2l_AB.nscf.out, dos.out 
Open the three output files and check that everything is o

3 files Band* should be there. 
You can use the the script plot_bands.py to plot them

python plot_bands.py 

At the end you should have a file Bande_AB-BG_vdW.png that is a png format
# 
