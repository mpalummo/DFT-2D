#!/bin/zsh
echo "starting scf+nscf calculation "
#mpirun pw.x <  bn_2l_AA1.scf.in > bn_2l_AA1.scf.out
#mpirun pw.x < bn_2l_AA1.nscf.in > bn_2l_AA1.nscf.out
echo "starting eps calculation "
mpirun epsilon.x < epsilon.in> epsilon.out
echo "calculation completed"
done
