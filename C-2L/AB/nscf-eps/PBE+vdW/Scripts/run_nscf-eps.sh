#!/bin/zsh
echo "starting scf+nscf calculation "
mpirun pw.x <  c_2l_AB.scf.in > c_2l_AB.scf.out
mpirun pw.x < c_2l_AB.nscf.in > c_2l_AB.nscf.out
echo "starting eps calculation "
mpirun epsilon.x < epsilon1.in> epsilon1.out
mpirun epsilon.x < epsilon2.in> epsilon2.out
echo "calculation completed"
done
