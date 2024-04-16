#
cd BN-1L/convergence/PBE/Vacuum

Copy the input files and Scripts to run and tp plot  from the two sub-directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file
run_vacuum.sh,  close it  and run doing:

./run_vacuum.sh

At the end you should several *out files 
Open some of them and check everything is ok

There should be also  files called avg*dat*

that reports self-consistent potential (without xc term) for each size of the cell along z (vacuum in the non periodic direction)

you can plot doing 

python plot_avgpot.py

At the end you should have the plot file  Avg_pot.png 

# 
