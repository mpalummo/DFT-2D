# enter in the directory AB

cd BN-2L/AA1/nscf-eps/PBE+vdW

Copy the input files and Scripts to run and tp plot  from the two sub-directories
cp ./Inputs/*in .
cp ./Scripts/* .

if your shell is not zsh substitute zsh with bash at the beginning of the script file
run_nscf-eps.sh,  close it  and run doing:

./run_nscf-eps.sh

At the end you should have 

Open them and check everything is ok

python plot_eps.py
