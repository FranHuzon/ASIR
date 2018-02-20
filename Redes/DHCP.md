# Peticiones DHCP.
Estructura de los mensajes que se envian al hacer una petición DHCP.

### DHCP Discovery.
- **Dirección:** Cliente --> Servidor.
- **Nivel de enlace:** Dirección MAC de difusión.
- **Nivel de red:** Dirección IP de difusión.
- **Nivel de transporte:** Puerto Destino 67/udp.


### DHCP Offer.
- Dirección: Servidor --> Cliente.
- Nivel de enlace: Dirección MAC del cliente.
- Nivel de red: Dirección IP de difusión.
- Nivel de transporte: Puerto Origen 67/udp, Puerto Destino 68/udp.


### DHCP Request.
- Dirección: Cliente --> Servidor.
- Nivel de enlace: Dirección MAC del servidor.
- Nivel de red: Dirección IP del servidor.
- Nivel de transporte: Puerto Destino 67/udp.


### DHCP ACK.
- Dirección: Servidor --> Cliente.