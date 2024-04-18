#
cd BN-1L/nscf-dos-stm/PBE+vdW

Copy the input files and script to run and plot  from the two directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script files
run_nscf-dos_k.sh and  run_nscf-dos_stm.sh. 

The first script performs one scf calculation and several nscf and dos calculations using different k-grids to check convergence over k-points. 
Open look at it, then close and run in this way:


./run_nscf-dos_k.sh 

At the end you should find several hBN*DOS* files calculated with different k-grids
you can plot them using the python script plot_dos_k.py

python plot_dos_k.py 

you will find a file dos_vs_kpt_bn_1l_PBE_vdW.png 

The second script performs first one scf calculation, then one nscf calculation with the selected k-grid at convergence and then again a dos calculation and also an STM image as post-processing

N.B.:  before running th script ./run_nscf-dos-stm.sh, you have to open bn_1l.nscf.in and substitute the 16 16 1 with 60 60 1 k-grid, close and svae the file and run it.

./run_nscf-dos-stm.sh

At the end you should have bn_1l.scf.out, bn_1l.nscf.out, dos.out 
and stm.out 

Open the output files and check that everything is ok.

You can use the script plot_bands_dos.py to plot  the bands calculated before togheter with the dos 

python plot_bands_dos.py 

you should find a file Bands_dos_bn_1l_PBE_vdW.png  to see the figure 

Finally you can use xcrysden --xsf  hBN_1l_PBE_vdW_stm.xsf
to plot the STM images, select  the Plane #1
If you want to learn doing more sofisticated images look at
https://aoterodelaroza.github.io/critic2/
# 
