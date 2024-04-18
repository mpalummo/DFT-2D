#
cd C-1L/nscf-dos/PBE+vdW

Copy the input files and script to run and plot  from the two directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file
run_nscf-dos_k.sh 

The first script performs one scf calculation and several nscf and dos calculations using different k-points grids to check convergence over k-points. 

./run_nscf-dos_k.sh 

At the end you should find several C*DOS* files calculated with different k-grid
you can plot them using the pyhton script plot_dos_k.py

python plot_dos_k.py 

Open the output files and check that everything is ok

You can use the the script plot_bands_dos.py to plot  the bands calculated before togheter with the dos 

python plot_bands_dos.py 

you should find a file band*png open and look at the figure

Finally you can use xcrysden --xsf  C2L_AB_PBE_vdW_stm.xsf
to plot the STM images along the Plane #1

# 
