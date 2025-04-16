set terminal pngcairo enhanced size 15cm,10cm
set output 'ecut_pbe_zoom.png'

set xlabel 'ecut [Ry]'
set ylabel 'E_{tot} [eV]'

set ytics 0.05
emin = -24.05451106*13.6057
set yrange [emin-0.05:emin+0.11]
f(x) = (-24.05451106*13.6057) + 0.01
g(x) = (-24.05451106*13.6057) + 0.1

plot 'Etot_vs_ecut_PBE.dat' u 1:($2*13.6057) w lp pt 7 ps 2 notitle, f(x) w l lw 2 t'+10 meV' , g(x) w l lw 2 t'+100 meV'

set output
set term pop
