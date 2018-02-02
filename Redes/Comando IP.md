### ip a
Muestra información de todas las interfaces disponibles.
~~~
jesus@debian:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master br0 state UP group default qlen 1000
    link/ether f0:79:59:2e:fb:09 brd ff:ff:ff:ff:ff:ff
3: wlan0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
    link/ether 7e:9a:91:26:32:b3 brd ff:ff:ff:ff:ff:ff
4: br0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether f0:79:59:2e:fb:09 brd ff:ff:ff:ff:ff:ff
    inet 172.22.8.32/16 brd 172.22.255.255 scope global br0
       valid_lft forever preferred_lft forever
    inet6 fe80::f279:59ff:fe2e:fb09/64 scope link 
       valid_lft forever preferred_lft forever
jesus@debian:~$ 
~~~