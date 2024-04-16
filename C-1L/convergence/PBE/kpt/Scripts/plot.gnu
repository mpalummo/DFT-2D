set terminal pngcairo enhanced size 25cm,20cm
set output 'Etot_vs_kpt.png'

set xlabel 'k-points'
set ylabel 'E_{tot} [eV]'

set ytics 0.05
emin = -23.42445150*13.6057
set yrange [emin-0.05:emin+0.05]
f(x) = (-23.42445150*13.6057) - 0.01
g(x) = (-23.42445150*13.6057) + 0.01

plot 'Etot_vs_kpt.dat' u 1:($2*13.6057) w lp pt 7 ps 2 notitle, f(x) w l lw 2 t'-10 meV' , g(x) w l lw 2 t'+10 meV'

set output
set term pop
