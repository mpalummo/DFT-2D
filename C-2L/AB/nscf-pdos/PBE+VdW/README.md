# cd AB/bands/PBE+vdW

Copy the input files and script to run and plot  from the two directories
cp ./Inputs/*in .
cp ./Scripts/* . 
# if your shell is not zsh substitute zsh with bash at the beginning of the script file
run_bands.sh  close and run

./run_nscf-pdos.sh

At the end you should have c_2l_AB.scf.out c_2l_AB.nscf.out pdos.out 
Open them and check that everything is ok

Several files called C2L_AB_PBE_vdW_DOS.dat.pdos* should be there. 
Check here https://www.quantum-espresso.org/Doc/INPUT_PROJWFC.html#idm100
how the different angular components are reported in the files.

You can use the script plot_pdos.py to plot p_x,p_y,p_z,s of the 4 Carbon atoms

python plot_pdos.py 

At the end you should have a file pdos60kpt_graphene_PBE_vdW.png  in a png format
# 
