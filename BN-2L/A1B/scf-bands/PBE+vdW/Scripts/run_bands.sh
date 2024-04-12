#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x <  bn_2l_A1B.scf.in > bn_2l_A1B.scf.out
mpirun pw.x <  bn_2l_A1B.bands.in > bn_2l_A1B.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

