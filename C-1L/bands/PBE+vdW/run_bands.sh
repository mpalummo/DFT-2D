#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x < c_1l.bands.in > c_1l.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

