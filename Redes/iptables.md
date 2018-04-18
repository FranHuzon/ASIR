Estructura:
Tablas --> Cadenas --> Reglas

Se divide en cuatro tablas:
	- filter
	- nat
		- PREROUTING
		- POSTROUTING
		- OUTPUT
		- INPUT
	- mangle
	- raw

Estructura reglas SNAT:
iptables -t {tabla} -A {cadena} {definición objetivo} {acción}
iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -o eth0 -j SNAT --to 172.22.x.y
iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -o eth0 -j MASQUERADE

Parámetros:
	-A: Añade las reglas al final
	-I: Añade las reglas al principio
	-s: Indica la dirección IP de origen
	-o: Indica la interfaz de salida
	-j: Define acciones
		--to (SNAT): Indica la dirección IP por la que se va a cambiar la dirección IP de origen

Ver reglas:
iptables -t {tabla} -L {cadena} -n -v --line-numbers


Eliminar reglas:
iptables -t {nat} -D {cadena} -s 10.0.0.0/24 -o eth0 -j SNAT --to 172.22.x.y --> Elimina una regla concreta
iptables -t {nat} -F {cadena} --> Elimina todas las reglas de la cadena

Estructura reglas DNAT:
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -d 172.22.x.y -j DNAT --to 10.0.0.2
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 8080 -d 172.22.x.y -j DNAT --to 10.0.0.2:80

Parámetros:
	-p: Indica el protocolo
	--dport: Indica el puerto destino
	-d: Indica la dirección IP destino

Hacer cambios persistentes:
Forma nº 1:	
- iptables-save > {fichero}
- iptables-restore < {fichero}

Forma nº 2:
- iptables-save > {fichero}
- apt install iptables-persistent