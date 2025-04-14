#!/bin/zsh

for i in  20 30 40 50 60 70 80 90 100
do

ecut=$i
echo "starting calculation for ecut = $ecut"

sed "s/ecutwfc = 20/ecutwfc = $ecut/" c_1l.scf.in > ecut_$ecut.in

mpirun pw.x < ecut_$ecut.in > ecut_$ecut.out

rm -rf tmp

echo "calculation for ecut = $ecut completed"

done

grep '!  ' *.out >> ecuttmp.dat
sed -i '' -e "s/ecut_//" ecuttmp.dat
sed -i '' -e "s/.out:!    total energy              =//" ecuttmp.dat

sort -n ecuttmp.dat > Etot_vs_ecut_PBE.dat
rm ecuttmp.dat
