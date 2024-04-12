#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x <  bn_2l_AB.scf.in > bn_2l_AB.scf.out
mpirun pw.x <  bn_2l_AB.bands.in > bn_2l_AB.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

