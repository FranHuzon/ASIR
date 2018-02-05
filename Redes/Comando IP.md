## ip address
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


## ip tuntap
Permite administrar interfaces tun/tap.


### add 
Crear interfaces tun/tap.
~~~
root@debian:# ip tuntap add mode {modo} user {usuario}
root@debian:# ip tuntap add mode {modo} user {usuario}
~~~


### del
Eliminar interfaces tun/tap.
~~~
root@debian:# ip tuntap del dev {interfaz} mode {modo}
root@debian:# ip tuntap del dev {interfaz} mode {modo}
~~~


### list
Muestra las interfaces tun/tap existentes.
~~~
root@debian:# ip tuntap list
tap0: tap UNKNOWN_FLAGS:800 user 1001
tun0: tun UNKNOWN_FLAGS:800 user 1001
root@debian:# 
~~~


## ip link set
Permite administrar las interfaces existentes.


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


## ip link add
Permite crear interfaces virtuales.

### type bond
Permite crear interfaces virtuales de tipo bonding.
~~~
root@debian:# ip link add name {interfaz} type 
~~~