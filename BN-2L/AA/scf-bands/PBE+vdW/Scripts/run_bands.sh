#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x <  bn_2l_AA.scf.in > bn_2l_AA.scf.out
mpirun pw.x <  bn_2l_AA.bands.in > bn_2l_AA.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

