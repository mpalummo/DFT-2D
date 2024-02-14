set terminal pngcairo enhanced size 15cm,10cm
set output 'kpt_zoom.png'

unset yrange
set xtics 4
set ytics 0.05
set grid x
Ry_to_eV = 13.6057

set xlabel 'k grid'
set ylabel 'E_{tot} [eV]'
set ytics 0.01

stats "kpt.dat" u 1:2 nooutput
stats "kpt.dat" u (lastX=$1,lastY=$2) nooutput
elast = lastY*13.6057
set key out horizontal center top


f(x) = elast + 0.01
g(x) = elast - 0.01

plot 'kpt.dat' u 1:($2*13.6057) w lp pt 7 ps 2 notitle, f(x) w l lw 2 t'+10 meV' , g(x) w l lw 2 t'-10 meV'

set output
set term pop