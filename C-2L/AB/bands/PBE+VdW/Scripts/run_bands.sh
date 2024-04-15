#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x < c_2l_AB.scf.in > c_2l_AB.scf.out
mpirun pw.x < c_2l_AB.bands.in > c_2l_AB.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

