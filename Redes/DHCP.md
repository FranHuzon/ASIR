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


# Parámetros DHCP.
Lista de los parámetros configurables de un servidor DHCP.


- **default-lease-time:** Tiempo de concesión por defecto.
- **max-lease-time:** Tiempo de concesión máxima mientras se renove la concesión.


Lista de parámetros de un cliente DHCP.
- **renew:** Hora a la que el cliente pedirá al servidor DHCP renovar su concesión.
- **rebind:** Hora a la que el cliente, si no ha tenido respuesta a la renovación de concesión, envia la petición de renovación al broadcast.
- **expire:** Hora a la que el cliente, si no ha tenido respuesta a ninguna renovación de concesión, desecha su concesión.