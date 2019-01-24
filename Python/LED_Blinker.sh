#Owen and Luca's Pi Blinker

x=0
gpio mode 0 out
gpio mode 26  out

while [ $x -le 10 ]
do
	gpio write 0 1
	gpio write 26 0
	sleep .1
	gpio write 0 0
	gpio write 26 1
	x=$(( $x + 1))
	sleep .1
done

gpio write 0 0
gpio write 26 0
