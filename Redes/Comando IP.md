# ip address
Muestra información de toas las interfaces disponibles y permite administrarlas.
~~~
jesus@debian:~$ ip address
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether f0:79:59:2e:fb:09 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.2/24 brd 192.168.1.255 scope global eth0
       valid_lft forever preferred_lft forever
3: wlan0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
    link/ether 32:64:e7:ab:bb:df brd ff:ff:ff:ff:ff:ff
jesus@debian:~$ 
~~~


### add 
Añade una nueva dirección IP a una interfaz existente.
~~~
jesus@debian:~$ ip address add {dirección ip} {máscara de red} dev {interfaz}
~~~


### del
Elimina una dirección IP de una interfaz existente.
~~~
jesus@debian:~$ ip address del {dirección ip} {máscara de red} dev {interfaz}
~~~


# ip tuntap
Permite administrar interfaces tun/tap.


### add 
Crear interfaces tun/tap.
~~~
root@debian:~# ip tuntap add {interfaz} mode {modo} user {usuario}
~~~


### del
Eliminar interfaces tun/tap.
~~~
root@debian:~# ip tuntap del dev {interfaz} mode {modo}
~~~


### list
Muestra las interfaces tun/tap existentes.
~~~
root@debian:~# ip tuntap list
tap0: tap UNKNOWN_FLAGS:800 user 1001
tun0: tun UNKNOWN_FLAGS:800 user 1001
root@debian:~# 
~~~


# ip link
Permite administrar las interfaces existentes.


### add
Permite crear interfaces virtuales.
~~~
root@debian:~# ip link add name {interfaz} type {bond | bridge | macvlan | dummy | ifb | vlan}
~~~


### delete
Permite eliminar interfaces virtuales existentes.
~~~
root@debian:~# ip link delete dev {interfaz}
~~~


### up
Levanta una interfaz existente.
~~~
jesus@debian:~$ ip link set {interfaz} up
~~~


### down
Baja una interfaz existente.
~~~
jesus@debian:~$ ip link set {interfaz} down
~~~


### master
Establece un maestro a una interfaz existente.
~~~
root@debian:~# ip link set dev {interfaz} master {interfaz}
~~~


# Casos prácticos.

## Creación de un bridge con varias interfaces.
Creación del bridge.
~~~
root@debian:~# ip link add name br0 type bridge
~~~


Creación de las distintas interfaces.
~~~
root@debian:~# ip tuntap add tap0 mode tap user jesus
root@debian:~# ip tuntap add tap1 mode tap user jesus
root@debian:~# ip tuntap add tap2 mode tap user jesus
~~~


Añadir las interfaces al bridge.
~~~
root@debian:~# ip link set dev tap0 master br0
root@debian:~# ip link set dev tap1 master br0
root@debian:~# ip link set dev tap2 master br0
~~~


## Creación link aggregation de dos interfaces.
Creación del bonding.
~~~
root@debian:~# ip link add name bond0 type bond
~~~


Creación de las distintas interfaces.
~~~
root@debian:~# ip tuntap add tap0 mode tap user jesus
root@debian:~# ip tuntap add tap1 mode tap user jesus
~~~


Añadir las interfaces al bonding.
~~~
root@debian:~# ip link set dev tap0 master bond0
root@debian:~# ip link set dev tap1 master bond0
~~~


## Creación de distintas VLAN.
Creación de las interfaces VLAN.
~~~
root@debian:~# ip link add name eth0.1 link eth0 type vlan id 1
root@debian:~# ip link add name eth0.5 link eth0 type vlan id 5
~~~


Creación de las interfaces virtuales.
~~~
root@debian:~# ip tuntap add tap01 mode tap user jesus
root@debian:~# ip tuntap add tap05 mode tap user jesus
~~~


Creación de los distintos puentes.
~~~
root@debian:~# ip link add name br01 type bridge
root@debian:~# ip link add name br05 type bridge
~~~


Añadir las distintas interfaces a sus respectivos bridges.
~~~
root@debian:~# ip link set dev eth0.1 master br01
root@debian:~# ip link set dev tap01 master br01
root@debian:~# ip link set dev eth0.5 master br05
root@debian:~# ip link set dev tap05 master br05
~~~