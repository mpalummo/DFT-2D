#!/bin/bash
LANG=en_US

gnuplot -persist <<-EOFMarker

set multiplot layout 2,1

list(start,end,increment)=system(sprintf("seq %.4f %.4f %.4f", start, increment, end))
plot for [i in list(0.2100,0.2700,0.01)] 'avg_'.i.'.dat' u 1:2 w l lw 2 t''.i.''

set yrange [0.384:0.391]
plot for [i in list(0.2100,0.2700,0.01)] 'avg_'.i.'.dat' u 1:2 w l lw 2 t''.i.''

unset multiplot
EOFMarker