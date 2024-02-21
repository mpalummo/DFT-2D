#!/bin/bash
LANG=en_US

gnuplot -persist <<-EOFMarker

set multiplot layout 2,1

list(start,end,increment)=system(sprintf("seq %.9f %.9f %.9f", start, increment, end))
plot for [i in list(3.400920045,4.800920045,0.2)] 'avg_'.i.'.dat' u 1:2 w l lw 2 t''.i.''

set yrange [0.2:0.7]
plot for [i in list(3.400920045,4.800920045,0.2)] 'avg_'.i.'.dat' u 1:2 w l lw 2 t''.i.''

unset multiplot
EOFMarker