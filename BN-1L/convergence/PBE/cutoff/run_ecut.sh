#!/bin/bash

for i in  20 30 40 50 60 70 80 90 100
do

ecut=$i
echo "starting calculation for ecut = $ecut"

sed "s/ecutwfc = 20/ecutwfc = $ecut/" bn_1l.scf.in > ecut_$ecut.in

pw.x < ecut_$ecut.in > ecut_$ecut.out

rm -fr tmp

echo "calculation for ecut = $ecut completed"

done

grep '!  ' *.out >> ecuttmp.dat
sed -i "s/ecut_//" ecuttmp.dat
sed -i "s/.out:!    total energy              =//" ecuttmp.dat

sort -n ecuttmp.dat > ecut.dat
rm ecuttmp.dat
