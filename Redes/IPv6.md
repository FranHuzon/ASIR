# Tipos de direcciones.
### Globales (Global)
- Rengo de direcciones para documentación: ``2001:db8::/32``


### Enlace local (Link Local)
EUI-64 y generación pseudo-aleatoria.


### Multicast
- Dirección multicast nodos: ``ff02::1``
- Dirección multicast routers: ``ff02::2``
- Dirección multicast DHCP: ``ff02::1:2``


# Neighbour Discovery.
ICMPv6 y direcciones multicast. Paquetes Router Solicitation, Router Advertisement, Network Solicitation, Network Advertisement.


# Configuración.
Configuración de una interfaz IPv6 de forma estática, dinámica y SLAAC.


### Configuración estática.
Configuración del fichero ``/etc/network/interfaces``.
~~~
auto {interfaz}
iface {interfaz} inet6 static
	address 2001:db8::2/128
	gateway 2001:db8::1 
~~~


Configuración del fichero ``/etc/resolv.conf``.
~~~
nameserver 2001:db8::1
~~~


### Configuración dinámica (DHCPv6).
Configuración del fichero ``/etc/network/interfaces``.
Stateful configuration, el servidor anota la concesión.
~~~
auto {interfaz}
iface {interfaz} inet6 dhcp
~~~


### Configuración SLAAC (Stateless Address Autoconfiguration).
Envia paquetes Network solicitation y Network advertisement para evitar la duplicidad de direcciones IP.
Cada cierto tiempo se solicita a la dirección multicast de routers los parametros de red (Router solicitation).
Una vez recibida la petición el router responde (Router advertisement).