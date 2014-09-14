#!/bin/sh

data="/usr/lib/cgi-data/tracercise.data"

select() {
	<$data awk -v tracer=$1 -v x=$2 -f /usr/lib/cgi-bin/tracercise.awk > "$data.$1"
}

plot() {
	</usr/lib/cgi-bin/tracercise.plot gnuplot > /dev/null 2>&1
}

output() {
cat<<EOF
Content-type: text/html

<html> 
<head>
<title>tracercise</title>
</head>
<body>
<h1>tracercise</h1>
<p>$1</p>
<img src="/tracercise/tracercise.png"></img>
</body> 
</html>
EOF

}

record() {
	entry=$(<$data grep "$1 $2")
	if [ -z "$entry" ]; then
		echo "$1 $2" >> $data
		select "r" 2
		select "b" 1
		plot
		output "Traced $1 $2"
	else
		output "Already traced $1 $2"
	fi
}

if [ "b" = "$1" ] || [ "r" = "$1" ]; then
	record "$1" "$(date -d "today 00:00" +%s)"
else
	output "Unknown tracer $1"
fi
