### ip a
Muestra información de toas las interfaces disponibles.
~~~
jesus@debian:~$ ip a
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


### ip a add
Añade una nueva dirección IP a una interfaz existente.
~~~
jesus@debian:~$ ip a add 192.168.1.3/24 dev eth0
~~~


### ip a del
Elimina una dirección IP de una interfaz existente.
~~~
jesus@debian:~$ ip a del 192.168.1.3/24 dev eth0
~~~

### ip l set
Levanta o baja una tarjeta existente.
~~~
jesus@debian:~$ ip l set eth0 up
jesus@debian:~$ ip l set eth0 down
~~~


### ip tuntap add
Crea interfaces tun e interfaces tap indicando el usuario propietario de dicha interfaz.
~~~
root@debian:# ip tuntap add mode tun user jesus
root@debian:# ip tuntap add mode tap user jesus
~~~


### ip tuntap list
Muestra las interfaces tun/tap existentes y su usuario propietario (UID).
~~~
oot@debian:# ip tuntap list
tap0: tap UNKNOWN_FLAGS:800 user 1001
tun0: tun UNKNOWN_FLAGS:800 user 1001
root@debian:# 
~~~


### ip tuntap del
Elimina interfaces tun/tap existentes.
~~~
root@debian:# ip tuntap del dev tun0 mode tun
root@debian:# ip tuntap del dev tap0 mode tap
~~~