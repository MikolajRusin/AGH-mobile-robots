#!/usr/bin/env bash

flag=$1
shift

case $flag in
	--port_number) 
		PORT_NUMBER=$1
		;;
	*)
		echo "not recognized $flag"
		exit 1
		;;
esac

python3 -m serial.tools.miniterm /dev/pts/$PORT_NUMBER 115200
