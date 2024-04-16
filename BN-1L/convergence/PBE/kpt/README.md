#
cd BN-1L/convergence/PBE/kpt

Copy the input files and Scripts to run and tp plot  from the two sub-directories
cp ./Inputs/*in .
cp ./Scripts/* . 

if your shell is not zsh substitute zsh with bash at the beginning of the script file
run_kpt.sh,  close it  and run doing:

./run_kpt.sh

At the end you should several *out files 
Open some of them and check everything is ok

There should be also a file called Etot_vs_kpt1.dat

that reports Etot versus k-grids  in Ry 

You can do the plot in 3 ways

python econv.py
python econv1.py
or using plot.gnu

you have to do  gnuplot
gnuplot> load 'plot.gnu'
gnuplot> quit


At the end you should produce a file called Etot_vs_kpt.png 

# 
