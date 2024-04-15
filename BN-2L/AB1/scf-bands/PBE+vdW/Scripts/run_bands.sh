#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x <  bn_2l_AB1.scf.in > bn_2l_AB1.scf.out
mpirun pw.x <  bn_2l_AB1.bands.in > bn_2l_AB1.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

