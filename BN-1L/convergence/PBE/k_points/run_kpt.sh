#!/bin/bash

for i in  4 8 12 16 20 24 28 32
do

kpt=$i
echo "starting calculation for kpt = $kpt"

sed "s/3 3 1 0 0 0/$kpt $kpt 1 0 0 0/" bn_1l.scf.in > kpt_$kpt.in

pw.x < kpt_$kpt.in > kpt_$kpt.out

rm -fr tmp

echo "calculation for kpt = $kpt completed"

done

grep '!  ' *.out >> kpttmp.dat
sed -i "s/kpt_//" kpttmp.dat
sed -i "s/.out:!    total energy              =//" kpttmp.dat

sort -n kpttmp.dat > kpt.dat
rm kpttmp.dat
