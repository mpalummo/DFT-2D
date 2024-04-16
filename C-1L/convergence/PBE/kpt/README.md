# Convergence on the kinetic energy cutoff
  cd   C-1L/vc-relax/PBE/kpt
  cp ./Inputs/* .
  cp ./Scripts/* .

# Use the script run_kpt.sh which prepares the inputs and run pw.x at different k-grids

At the end you should obtain Etot_vs_kpt.dat

You can plot it is using one of the python scripts you copied from 
the Script directory or using plot.gnu
both procedures will create png files. 
