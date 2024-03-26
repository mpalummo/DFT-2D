set terminal pngcairo enhanced size 15cm,10cm
set output 'kpt_zoom.png'

unset yrange 

set xlabel 'k grid'
set ylabel 'E_{tot} [eV]'

set ytics 0.05
emin = -23.41246875*13.6057

f(x) = emin + 0.01
g(x) = emin - 0.01

plot 'kpt.dat' u 1:($2*13.6057) w lp pt 7 ps 2 notitle, f(x) w l lw 2 t'+10 meV' , g(x) w l lw 2 t'-10 meV'

set output
set term pop
