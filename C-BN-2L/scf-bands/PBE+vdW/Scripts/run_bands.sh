#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x < cbn_2l_AB.scf.in > cbn_2l_AB.scf.out 
mpirun pw.x <  cbn_2l_AB.bands.in > cbn_2l_AB.bands.out 
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

