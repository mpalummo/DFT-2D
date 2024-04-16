#
cd AB/nscf-dos-stm/PBE+vdW

Copy the input files and script to run and plot  from the two directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script files
run_nscf-dos_k.sh and  run_nscf-dos_stm.sh. 

The first script performs one scf calculation and several nscf and dos calculations using different k-points grids to check convergence over k-points. 

./run_nscf-dos_k.sh 

At the end you should find several C*DOS* files calculated with different k-grid
you can plot them using the pyhton script plot_dos_k.py

python plot_dos_k.py 

The second script runs first one scf calculation, the one nscf calculation with the selected k-grid at convergence and then again a dos calculation and also an STM image as post-processing

So, before running the script, you have to open c_2l_AB.nscf.in and substitute the 12 12 1 with 60 60 1 k-grid and close the file

./run_nscf-dos-stm.sh

At the end you should have c_2l_AB.scf.out, c_2l_AB.nscf.out, dos.out 
and stm.out 

Open the output files and check that everything is ok

You can use the the script plot_bands_dos.py to plot  the bands calculated before togheter with the dos 

python plot_bands_dos.py 

you should find a file bands-dos_AB-BG_PBE_vdW.png open and look at the figure

Finally you can use xcrysden --xsf  C2L_AB_PBE_vdW_stm.xsf
to plot the STM images along the Plane #1

# 
