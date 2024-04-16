# Convergence on the kinetic energy cutoff
  cd   C-1L/vc-relax/PBE/cutoff
  cp ./Inputs/* .
  cp ./Scripts/* .

# Use the script run_ecut.sh which prepares the inputs and run pw.x at different ecut

At the end you should obtain  Etot_vs_ecut_PBE.dat

You can plot is using one of the python scripts you copied from the Script directory or using plot.gnu
both procedures will create png files. 
