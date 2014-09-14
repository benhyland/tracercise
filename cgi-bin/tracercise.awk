BEGIN { lastTime = -1; }

tracer == $1 {
		if(lastTime != -1 && ($2 - lastTime) > 86400) {
			print ""
		}
		lastTime = $2;
		print $2 " " x;
}
