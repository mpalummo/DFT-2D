#!/bin/zsh

for i in AA1 AB  
do

stack=$i
echo "starting calculation for stack = $i"

grep '!    total energy ' ./$stack/PBE+vdW/bn_2l_$stack.vc-relax.out >> etot_$stack.out
sed "s/!    total energy              = /$stack/"  etot_$stack.out  > etot_vs_$stack.dat
sort -r etot_vs_$stack.dat > etot_vs_$stack.dat.sort
done

