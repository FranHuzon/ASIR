#!/bin/bash

renovar_ip() {
	while true
		do
			dhclient -r $interfaz
			dhclient $interfaz
			sleep 60
		done
}

escribir_fichero() {
	variable=`ip a | grep $interfaz | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' | grep -v '255'`
	if [[ ! -s comprobIP.txt ]]
		then
			echo $variable > comprobIP.txt
	fi
}