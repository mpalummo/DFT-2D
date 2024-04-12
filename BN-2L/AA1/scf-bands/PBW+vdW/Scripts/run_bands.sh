#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x <  bn_2l_AA1.scf.in > bn_2l_AA1.scf.out
mpirun pw.x <  bn_2l_AA1.bands.in > bn_2l_AA1.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

