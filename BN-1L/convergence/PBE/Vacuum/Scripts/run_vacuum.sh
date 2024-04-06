#!/bin/zsh

for i in 4 5 6 7 8 
do

cellz=$i
c=$((4.635*i))
echo ${c}
echo "starting calculation for celldm(3) = $cellz"

sed "s/celldm(3) = 6/celldm(3) = $cellz/" bn_1l.scf.in > bn_1l.scf_$c.in

pw.x < bn_1l.scf_$c.in > bn_1l.scf_$c.out
pp.x < pp.in > pp.out
average.x < average.in > average.out

rm -fr tmp

echo "calculation for celldm(3) = $cellz completed"
mv avg.dat avg.dat_$c
done

grep '!  ' *.out >> etotv_tmp.dat
sed -i '' -e "s/bn_1l.scf_//" etotv_tmp.dat
sed -i '' -e "s/.out:!    total energy              =//" etotv_tmp.dat


sort -n etotv_tmp.dat > Etot_vs_vac_PBE.dat
rm etotv_tmp.dat
