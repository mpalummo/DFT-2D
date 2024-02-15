#!/bin/bash
LANG=en_US
#it should be en_US.UTF-8
LC_NUMERIC=de_DE.UTF-8

for i in  $(seq 0.2100 0.01 0.2700)
do

z=$i
echo "starting  scf calculation for celldm(3) = $z"
sed "s/0.250000000/$z/" c_2l_AA.scf.in > $z.in

pw.x < $z.in > $z.out &&

echo "starting  pp.x calculation for celldm(3) = $z"
pp.x < pp.in > pp.out &&

echo "starting  average.x calculation for celldm(3) = $z"
average.x < average.in > average.out &&

cp avg.dat avg_$z.dat
rm -fr tmp

echo "calculation for kpt = $z completed"

done

grep '!  ' *.out >> vacuum_tmp.dat

sed -i "s/.out:!    total energy              =//" vacuum_tmp.dat

sort -n vacuum_tmp.dat > vacuum.dat
rm vacuum_tmp.dat
