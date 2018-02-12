# Generar dirección MAC.
Para que las interfaces de nuestra máquina virtual puedan funcionar correctamente deberán tener una dirección MAC válida, deberemos generar una dirección MAC por cada interfaz que queramos utilizar.
~~~
jesus@debian:~$ MAC0=$(echo "02:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)
~~~


# Aprovisionamiento ligero.
El aprovisionamiento ligero permite crear varias máquinas virtuales a partir de una misma imagen base.
~~~
jesus@debian:~$ qemu-img create -b {imagen base} -f qcow2 {imagen MV}
~~~


# Lanzar MV.
Una vez hemos creado una nueva imagen y disponemos de una o varias interfaces con sus direcciones MAC correspondientes, podemos lanzar nuestra máquina virtual.
~~~
jesus@debian:~$ kvm -m {memoria RAM} -hda {imagen} -device virtio-net,netdev=n{numero intefaz},mac={variable MAC} -netdev tap,id=n{numero interfaz},ifname={nombre interfaz},script=no,downscript=no
~~~


En el caso de que queramos lanzar una máquina virtual con varias interfaces de red, deberemos repetir los siguiente parámetros cambiando tanto el número de la interfaz, como la dirección MAC y el nombre de la interfaz.


### Ejemplo.
Vamos a lanzar una máquina virtual con las siguiente características:
- Memoria RAM: 512MB
- Imagen: mv1.qcow2
- Primera interfaz: tap0
- Primera interfaz (MAC): $MAC0
- Segunda interfaz: tap1
- Segunda interfaz (MAC): $MAC1


Para ello ejecutaremos el siguiente comando:
~~~
jesus@debian:~$ kvm -m 512 -hda mv1.qcow2 -device virtio-net,netdev=n0,mac=$MAC0 -netdev tap,id=n0,ifname=tap0,script=no,downscript=no -device virtio-net,netdev=n1,mac=$MAC1 -netdev tap,id=n1,ifname=tap1,script=no,downscript=no
~~~