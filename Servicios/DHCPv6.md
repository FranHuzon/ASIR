# Peticiones DHCPv6.
Estructura de los mensajes que se envian en una petición DHCPv6.


### DHCPv6 Solicit.
- **Dirección:** Cliente --> Servidor.
- **Nivel de red:** Dirección multicast DHCP.
- **Nivel de transporte:** Puerto Destino 547/udp.


### DHCPv6 Advertise.
- **Dirección:** Servidor --> Cliente.
- **Nivel de red:** Dirección de enlace local del cliente.
- **Nivel de transporte:** Puerto Origen 547/udp, Puerto Destino 546/udp.


### DHCPv6 Request.
- **Dirección:** Cliente --> Servidor.
- **Nivel de red:** Dirección multicast DHCP.
- **Nivel de transporte:** Puerto Destino 547/udp.


### DHCPv6 Confirm.
- **Dirección:** Servidor --> Cliente.
- **Nivel de red:** Dirección de enlace local del cliente.
- **Nivel de transporte:** Puerto Destino 547/udp, Puerto Origen 546/udp.