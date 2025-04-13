#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x < C-2L-EF-AB.scf.in > C-2L-EF-AB.scf.out 
mpirun pw.x < C-2L-EF-AB.bands.in > C-2L-EF-AB.bands.out
mpirun bands.x < C-2L-EF-AB.bandspp.in > C-2L-EF-AB.bandspp.out

echo "calculation completed"

