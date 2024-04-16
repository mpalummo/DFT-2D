#
cd AA/nscf-dos-stm/PBE+vdW

Copy the input files and script to run and plot  from the two directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file
 run_nscf-dos_stm.sh. 

Now you can run the script to do a scf, nscf and dos and stm calculations

./run_nscf-dos-stm.sh

At the end you should have c_2l_AA.scf.out, c_2l_AA.nscf.out, dos.out 
and stm.out 

Open the output files and check that everything is ok

You can use the the script plot_bands_dos.py to plot  the bands calculated before togheter with the dos 

python plot_bands_dos.py 

you should find a file bands-dos_AA-BG_PBE_vdW.png open and look at the figure

Finally you can use xcrysden --xsf  C2L_AA_PBE_vdW_stm.xsf
to plot the STM images along the Plane #1

# 
