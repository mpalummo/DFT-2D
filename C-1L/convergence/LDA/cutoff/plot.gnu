set terminal pngcairo enhanced size 15cm,10cm
set output 'ecut.png'

unset yrange
set xtics auto
set ytics auto
set grid x

Ry_to_eV = 13.6057

set xlabel 'ecut [Ry]'
set ylabel 'E_{tot} [eV]'

stats "ecut.dat" u 1:2 nooutput
stats "ecut.dat" u (lastX=$1,lastY=$2) nooutput
elast = lastY*13.6057

set yrange [elast:elast+2]
set key out horizontal center top

f(x) = elast + 0.1
g(x) = elast + 0.01

plot 'ecut.dat' u 1:($2*13.6057) w lp pt 7 ps 2 notitle, f(x) w l lw 2 t'-100 meV' , g(x) w l lw 2 t'-10 meV'

set output
set term pop
