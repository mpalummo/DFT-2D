#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x < c_2l_AA.bands.in > c_2l_AA.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

