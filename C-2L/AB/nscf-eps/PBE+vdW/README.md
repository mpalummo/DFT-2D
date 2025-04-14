#
cd AB/nscf-eps/PBE+vdW

Copy the input files and script to run and plot  from the two directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file
run_nscf-eps.sh  

The first script performs one scf calculation and several nscf and epsilon calculations using different k-points grids to check convergence over k-points. 

./run_nscf-eps_k.sh 

you can plot the spectra using the pyhton script plot_eps_k.py

python plot_eps_k.py 

# 
