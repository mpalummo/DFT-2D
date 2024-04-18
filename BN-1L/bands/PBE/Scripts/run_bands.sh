#!/bin/zsh

echo "starting bands calculation "

mpirun pw.x < bn_1l.scf.in > bn_1l.scf.out
mpirun pw.x < bn_1l.bands.in > bn_1l.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

