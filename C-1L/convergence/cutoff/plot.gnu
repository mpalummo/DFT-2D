set terminal pngcairo enhanced size 15cm,10cm
set output 'ecut_zoom.png'

set xlabel 'ecut [Ry]'
set ylabel 'E_{tot} [eV]'

set ytics 0.05
emin = -22.75542228*13.6057
set yrange [emin:emin+0.2]
f(x) = (-22.75542228*13.6057) + 0.01
g(x) = (-22.75542228*13.6057) + 0.1

plot 'ecut.dat' u 1:($2*13.6057) w lp pt 7 ps 2 notitle, f(x) w l lw 2 t'+10 meV' , g(x) w l lw 2 t'+100 meV'

set output
set term pop