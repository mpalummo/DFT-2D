# cd C-BN-2L/nscf-pdos/PBE+VdW 

Copy the input files and script to run and plot  from the two directories
cp ./Inputs/*in .
cp ./Scripts/* . 

# if your shell is not zsh substitute zsh with bash at the beginning of the script file close and run it

./run_nscf-pdos.sh

At the end you should have cbn_2l_AB.scf.out cbn_2l_AB.nscf.out pdos.out 
Open them and check that everything is ok

Several files called C2L_AB_PBE_vdW_DOS.dat.pdos* should be there. 
Check here https://www.quantum-espresso.org/Doc/INPUT_PROJWFC.html#idm100
how the different angular components are reported in the files.

You can use the script plot_pdos.py to plot the contribution to the DOS of p_z,of the 2 C atoms and B and N 

python plot_pdos.py 

At the end you should have a file pdos60*.png  in a png format

You can also plot Bands calculated before togheter PDOS

python plot_bands_pdos.py
# 
