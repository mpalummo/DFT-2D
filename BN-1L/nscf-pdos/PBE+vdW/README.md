# cd BN-1L/nscf-pdos/PBE+vdW

Copy the input files and scripts files to run and plot

cp ./Inputs/*in .
cp ./Scripts/* . 


if your shell is not zsh substitute zsh with bash at the beginning of the script file
 close and run

./run_nscf-pdos.sh

At the end you should have bn_1l.scf.out bn_1l.nscf.out pdos.out 
Open them and check that everything is ok

Several files called hBN_1L*.pdos* should be there. 
Check here https://www.quantum-espresso.org/Doc/INPUT_PROJWFC.html#idm100
to understand what they are and how the different angular components are reported in these files.

You can use the script plot_pdos.py to plot p_x,p_y,p_z,s contributions to the DOS of the B and N atoms in the 2 layers

python plot_pdos.py 

At the end you should have a file pdos60kpt_hBN_1L_PBE_vdW.png  in a png format

You can use another script plot_bands_pdos.py to plot the bandstructure togheter with the pdos
# 
