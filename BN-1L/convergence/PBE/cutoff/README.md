#
cd BN-1L/convergence/PBE/cutoff

Copy the input files and Scripts to run and tp plot  from the two sub-directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file
run_ecut.sh,  close it  and run doing:

./run_ecut.sh

At the end you should several *out files 
Open some of them and check everything is ok

There should be also a file called Etot_vs_ecut_PBE.dat

Now you can plot the Etot versus Energy cutoff in Ry in 3 ways


python econv.py
python econv1.py
or using plot.gnu

you have to do  gnuplot
gnuplot> load 'plot.gnu'
gnuplot> quit


At the end you should produce a file Etot_vs_ecut.png, with the first 2 scripts, or ecut_pbe_zoom.png using plot.gnu

# 
