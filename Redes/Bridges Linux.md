# Configuración


Para crear un nuevo bridge deberemos modificar el fichero ``/etc/network/interfaces``, en este caso crearemos el bridge **br0** que se configurará mediante un servidor **dhcp** y añadiremos la interfaz **eth0** a dicho puente:
~~~
auto br0
iface br0 inet dhcp
	bridge_ports eth0
~~~


En el caso de que usemos un portatil, cambiaremos la línea ``auto br0`` por la línea ``allow-hotplug br0`` para que cuando no estemos conectados a la red de forma cableada no intente levantar la interfaz y ralentice el arranque intentando configurarla.


Una vez hemos creado el bridge debemos asegurarnos de que en el fichero ``/etc/default/bridge-utils`` aparece la siguiente línea:
~~~
BRIDGE_HOTPLUG=yes
~~~


Por último, reiniciaremos la máquina, en el caso de que la interfaz **br0** no se levante automaticamente, tendremos que levantarla manualmente con el siguiente comando:
~~~
ifup br0
~~~


# Comandos


### brctl show
Muestra los bridges existentes y las interfaces que los componen.
~~~
root@debian:~# brctl show
bridge name	bridge id		STP enabled	interfaces
br0		8000.f079592efb09	no		eth0

~~~


### brctl addif
Añade una interfaz a un puente existente.
~~~
root@debian:~# brctl addif br0 eth0
~~~