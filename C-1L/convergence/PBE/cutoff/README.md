# Convergence on the kinetic energy cutoff
  cp ./Inputs/* .
  cp ./Scripts/* .

# Use the script run_ecut.sh which prepares the inputs and run pw.x at different kinetic energy cutoffs ecut

At the end you should obtain  Etot_vs_ecut_PBE.dat

You can plot it using one of the python scripts you copied from the Script directory or using plot.gnu
all the  procedures will create png files. 
