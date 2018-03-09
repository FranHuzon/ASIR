# Peticiones DHCP.
Estructura de los mensajes que se envian al hacer una petición DHCP.


### DHCP Discovery.
- **Dirección:** Cliente --> Servidor.
- **Nivel de enlace:** Dirección MAC de difusión.
- **Nivel de red:** Dirección IP de difusión.
- **Nivel de transporte:** Puerto Destino 67/udp.


### DHCP Offer.
- **Dirección:** Servidor --> Cliente.
- **Nivel de enlace:** Dirección MAC del cliente.
- **Nivel de red:** Dirección IP de difusión.
- **Nivel de transporte:** Puerto Origen 67/udp, Puerto Destino 68/udp.


### DHCP Request.
- **Dirección:** Cliente --> Servidor.
- **Nivel de enlace:** Dirección MAC del servidor.
- **Nivel de red:** Dirección IP del servidor.
- **Nivel de transporte:** Puerto Destino 67/udp.


### DHCP ACK.
- **Dirección:** Servidor --> Cliente.


# Instalación.
Instalación del servidor DHCP **isc-dhcp**.
~~~
root@debian:~# apt install isc-dhcp-server
~~~


# Ficheros de configuración.
Fichero de configuración del servicio ``/etc/dhcp/dhcpd.conf``.


Fichero de configuración del demonio ``/etc/default/isc-dhcp-server``.


# Parámetros.
Lista de parámetros de un servidor DHCP.

- **default-lease-time:** Tiempo de concesión por defecto.
- **max-lease-time:** Tiempo máximo de concesión.
- **ddns-update-style:** Crea un nuevo registro en el servidor DNS cuando se concede una IP.
- **option domain-name:** Nombre de dominio de la red.
- **option domain-name-servers:** Servidor/es DNS de la red.
- **authoritative:** Indica que es el servidor DHCP principal.
- **subnet:** Indica la dirección de red.
- **netmaks:** Indica la máscara de la red.
- **range:** Rango de direcciones IP que puede conceder el servidor.
- **option routers:** Indica la/s puerta/s de enlace.
- **option broadcast-addres:** Dirección de difusión de la red.
- **host:** Permite establecer reservas.
- **hardware ethernet:** Indica la dirección MAC de la máquina reserva.
- **fixed-address:** Indica la dirección IP reservada.

Lista de parámetros de un cliente DHCP.

- **renew:** Hora a la que el cliente pedirá al servidor DHCP renovar su concesión.
- **rebind:** Hora a la que el cliente, si no ha tenido respuesta a la renovación de concesión, envia la petición de renovación al broadcast.
- **expire:** Hora a la que el cliente, si no ha tenido respuesta a ninguna renovación de concesión, desecha su concesión.
- **supersede:** Cambia la configuración proporcionada por el servidor DHCP por la configuración indicada.
- **prepend:** Añade la configuración indicada por encima de la configuración proporcionada por el servidor DHCP.
- **append:**  Añade la configuración indicada por debajo de la configuración proporcionada por el servidor DHCP.