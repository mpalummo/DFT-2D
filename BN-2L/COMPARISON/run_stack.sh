#!/bin/zsh

for i in AA1 AB AA A1B AB1  
do

stack=$i
echo "starting calculation for stack = $i"

grep '!    total energy ' ./$stack/vc-relax/PBE+vdW/Ref/bn_2l_$stack.vc-relax.out >> etot_$stack.out
sed "s/!    total energy              = /$stack/"  etot_$stack.out  > etot_vs_$stack.dat
sort -r etot_vs_$stack.dat > etot_vs_$stack.dat.sort
sed -n -e 1p etot_vs_$stack.dat.sort > etot_vs_$stack.dat1
done
cat etot_vs_AA1.dat1 etot_vs_AB.dat1 etot_vs_AA.dat1 etot_vs_A1B.dat1 etot_vs_AB1.dat1 > etot_vs_stack.dat
