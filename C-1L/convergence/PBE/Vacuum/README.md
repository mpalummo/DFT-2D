# Convergence on the Vacuum along the non-periodic direction
  cd   C-1L/vc-relax/PBE/Vacuum
  cp ./Inputs/* .
  cp ./Scripts/* .

# Use the script run_vacuum.sh which prepares the inputs and run pw.x,pp.x and average.x 
using cells with different vacuum along the non periodic direction to calculate the electrostatic potential along the non-periodic direction of the cell

At the end you should obtain Etot_vs_vacuum.dat and several avg*dat* files

You can plot them  using the script plot_avgpot.py 
or plot.gnu
