set terminal png
set title "tracercise"
set output "/var/www/tracercise/tracercise.png"

set xdata time
set timefmt "%s"

unset ytics

set yrange [0:3]

plot "/usr/lib/cgi-data/tracercise.data.r" using 1:2 with circles fill solid t "r", "/usr/lib/cgi-data/tracercise.data.b" using 1:2 with circles fill solid t "b"
