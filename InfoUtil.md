# Puertos.

- **HTTP:** 80
- **HTTPS:** 443
- **DHCP:** 67, 68 (udp) 
- **SSH:** 22
- **DNS:** 53 (udp)
- **FTP:** 20, 21
- **mysql:** 3306
- **postgresql:** 5432
- **oracle:** 1521
- **DHCPv6:** 546, 547 (udp)


# Directorios y ficheros.

- ``/etc/{servicio}``: Ficheros de configuración de los distintos servicios. 
- ``/etc/default/{servicio}``: Ficheros de configuración de los demonios de los distintos servicios.
- ``/etc/hosts``: Fichero de resolución de nombres (Cuando no hay servidor DNS).
- ``/usr/share/doc``: Documentación de paquetes.
- `/proc/sys/net/ipv6/conf/{interfaz}`: Parámetros configurables de las distintas interfaces ipv6.