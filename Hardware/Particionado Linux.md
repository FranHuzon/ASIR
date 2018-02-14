# Particionado con fdisk.


Creación de distintos esquemas de particionado utilizando la herramienta **fdisk**.


## Primer esquema.
- Disco duro: 1 GB.
- Partición Primaria: 150 MB, Tipo Linux.
- Partición Lógica: Tipo Linux
- Partición Lógica: Tipo Linux
- Partición Lógica: Tipo ntfs
- Partición Lógica: Tipo FAT32
- Partición Lógica: Tipo swap.


Ejecución de **fdisk** indicando el disco a formatear.
~~~
root@debian:~# fdisk /dev/sdb

Bienvenido a fdisk (util-linux 2.29.2).
Los cambios solo permanecerán en la memoria, hasta que decida escribirlos.
Tenga cuidado antes de utilizar la orden de escritura.

El dispositivo no contiene una tabla de particiones reconocida.
Se ha creado una nueva etiqueta de disco DOS con el identificador de disco 0xe463b033.

Orden (m para obtener ayuda):
~~~
 

Creación de la partición primaria.
~~~
Orden (m para obtener ayuda): n
Tipo de partición
   p   primaria (0 primaria(s), 0 extendida(s), 4 libre(s))
   e   extendida (contenedor para particiones lógicas)
Seleccionar (valor predeterminado p): p
Número de partición (1-4, valor predeterminado 1): 1
Primer sector (2048-2097151, valor predeterminado 2048): 2048
Último sector, +sectores o +tamaño{K,M,G,T,P} (2048-2097151, valor predeterminado 2097151): +150M

Crea una nueva partición 1 de tipo 'Linux' y de tamaño 150 MiB.

Orden (m para obtener ayuda): p
Disco /dev/sdb: 1 GiB, 1073741824 bytes, 2097152 sectores
Unidades: sectores de 1 * 512 = 512 bytes
Tamaño de sector (lógico/físico): 512 bytes / 512 bytes
Tamaño de E/S (mínimo/óptimo): 512 bytes / 512 bytes
Tipo de etiqueta de disco: dos
Identificador del disco: 0x2744f900

Disposit.  Inicio Comienzo  Final Sectores Tamaño Id Tipo
/dev/sdb1             2048 309247   307200   150M 83 Linux

Orden (m para obtener ayuda): w
Se ha modificado la tabla de particiones.
Llamando a ioctl() para volver a leer la tabla de particiones.
Se están sincronizando los discos.
                                                   
root@debian:~# 
~~~


Creación de las distintas particiones lógicas.
~~~
root@debian:~# fdisk /dev/sdb

Bienvenido a fdisk (util-linux 2.29.2).
Los cambios solo permanecerán en la memoria, hasta que decida escribirlos.
Tenga cuidado antes de utilizar la orden de escritura.


Orden (m para obtener ayuda): n
Tipo de partición
   p   primaria (1 primaria(s), 0 extendida(s), 3 libre(s))
   e   extendida (contenedor para particiones lógicas)
Seleccionar (valor predeterminado p): e
Número de partición (2-4, valor predeterminado 2): 2
Primer sector (309248-2097151, valor predeterminado 309248): 
Último sector, +sectores o +tamaño{K,M,G,T,P} (309248-2097151, valor predeterminado 2097151): 

Crea una nueva partición 2 de tipo 'Extended' y de tamaño 873 MiB.

Orden (m para obtener ayuda): p
Disco /dev/sdb: 1 GiB, 1073741824 bytes, 2097152 sectores
Unidades: sectores de 1 * 512 = 512 bytes
Tamaño de sector (lógico/físico): 512 bytes / 512 bytes
Tamaño de E/S (mínimo/óptimo): 512 bytes / 512 bytes
Tipo de etiqueta de disco: dos
Identificador del disco: 0x2744f900

Disposit.  Inicio Comienzo   Final Sectores Tamaño Id Tipo
/dev/sdb1             2048  309247   307200   150M 83 Linux
/dev/sdb2           309248 2097151  1787904   873M  5 Extendida

Orden (m para obtener ayuda): n
Se está utilizando todo el espacio para particiones primarias.
Se añade la partición lógica 5
Primer sector (311296-2097151, valor predeterminado 311296): 
Último sector, +sectores o +tamaño{K,M,G,T,P} (311296-2097151, valor predeterminado 2097151): +175M

Crea una nueva partición 5 de tipo 'Linux' y de tamaño 175 MiB.

Orden (m para obtener ayuda): n
Se está utilizando todo el espacio para particiones primarias.
Se añade la partición lógica 6
Primer sector (671744-2097151, valor predeterminado 671744): 
Último sector, +sectores o +tamaño{K,M,G,T,P} (671744-2097151, valor predeterminado 2097151): +175M

Crea una nueva partición 6 de tipo 'Linux' y de tamaño 175 MiB.

Orden (m para obtener ayuda): n
Se está utilizando todo el espacio para particiones primarias.
Se añade la partición lógica 7
Primer sector (1032192-2097151, valor predeterminado 1032192): 
Último sector, +sectores o +tamaño{K,M,G,T,P} (1032192-2097151, valor predeterminado 2097151): +175M

Crea una nueva partición 7 de tipo 'Linux' y de tamaño 175 MiB.

Orden (m para obtener ayuda): n
Se está utilizando todo el espacio para particiones primarias.
Se añade la partición lógica 8
Primer sector (1392640-2097151, valor predeterminado 1392640): 
Último sector, +sectores o +tamaño{K,M,G,T,P} (1392640-2097151, valor predeterminado 2097151): +175M

Crea una nueva partición 8 de tipo 'Linux' y de tamaño 175 MiB.

Orden (m para obtener ayuda): n
Se está utilizando todo el espacio para particiones primarias.
Se añade la partición lógica 9
Primer sector (1753088-2097151, valor predeterminado 1753088): 
Último sector, +sectores o +tamaño{K,M,G,T,P} (1753088-2097151, valor predeterminado 2097151): 

Crea una nueva partición 9 de tipo 'Linux' y de tamaño 168 MiB.

Orden (m para obtener ayuda): p
Disco /dev/sdb: 1 GiB, 1073741824 bytes, 2097152 sectores
Unidades: sectores de 1 * 512 = 512 bytes
Tamaño de sector (lógico/físico): 512 bytes / 512 bytes
Tamaño de E/S (mínimo/óptimo): 512 bytes / 512 bytes
Tipo de etiqueta de disco: dos
Identificador del disco: 0x2744f900

Disposit.  Inicio Comienzo   Final Sectores Tamaño Id Tipo
/dev/sdb1             2048  309247   307200   150M 83 Linux
/dev/sdb2           309248 2097151  1787904   873M  5 Extendida
/dev/sdb5           311296  669695   358400   175M 83 Linux
/dev/sdb6           671744 1030143   358400   175M 83 Linux
/dev/sdb7          1032192 1390591   358400   175M 83 Linux
/dev/sdb8          1392640 1751039   358400   175M 83 Linux
/dev/sdb9          1753088 2097151   344064   168M 83 Linux

Orden (m para obtener ayuda): t
Número de partición (1,2,5-9, valor predeterminado 9): 7
Tipo de partición (teclee L para ver todos los tipos): l

 0  Vacía           24  DOS de NEC      81  Minix / Linux a bf  Solaris        
 1  FAT12           27  NTFS de WinRE o 82  Linux swap / So c1  DRDOS/sec (FAT-
 2  XENIX root      39  Plan 9          83  Linux           c4  DRDOS/sec (FAT-
 3  XENIX usr       3c  PartitionMagic  84  OS/2 oculto o h c6  DRDOS/sec (FAT-
 4  FAT16 <32M      40  Venix 80286     85  Linux extendida c7  Syrinx         
 5  Extendida       41  PPC PReP Boot   86  Conjunto de vol da  Datos sin SF   
 6  FAT16           42  SFS             87  Conjunto de vol db  CP/M / CTOS / .
 7  HPFS/NTFS/exFAT 4d  QNX4.x          88  Linux plaintext de  Utilidad Dell  
 8  AIX             4e  QNX4.x segunda  8e  Linux LVM       df  BootIt         
 9  AIX arrancable  4f  QNX4.x tercera  93  Amoeba          e1  DOS access     
 a  Gestor de arran 50  OnTrack DM      94  Amoeba BBT      e3  DOS R/O        
 b  W95 FAT32       51  OnTrack DM6 Aux 9f  BSD/OS          e4  SpeedStor      
 c  W95 FAT32 (LBA) 52  CP/M            a0  Hibernación de  ea  alineamiento Ru
 e  W95 FAT16 (LBA) 53  OnTrack DM6 Aux a5  FreeBSD         eb  BeOS fs        
 f  W95 Ext'd (LBA) 54  OnTrackDM6      a6  OpenBSD         ee  GPT            
10  OPUS            55  EZ-Drive        a7  NeXTSTEP        ef  EFI (FAT-12/16/
11  FAT12 oculta    56  Golden Bow      a8  UFS de Darwin   f0  inicio Linux/PA
12  Compaq diagnost 5c  Priam Edisk     a9  NetBSD          f1  SpeedStor      
14  FAT16 oculta <3 61  SpeedStor       ab  arranque de Dar f4  SpeedStor      
16  FAT16 oculta    63  GNU HURD o SysV af  HFS / HFS+      f2  DOS secondary  
17  HPFS/NTFS ocult 64  Novell Netware  b7  BSDI fs         fb  VMFS de VMware 
18  SmartSleep de A 65  Novell Netware  b8  BSDI swap       fc  VMKCORE de VMwa
1b  FAT32 de W95 oc 70  DiskSecure Mult bb  Boot Wizard hid fd  Linux raid auto
1c  FAT32 de W95 (L 75  PC/IX           bc  Acronis FAT32 L fe  LANstep        
1e  FAT16 de W95 (L 80  Minix antiguo   be  arranque de Sol ff  BBT            
Tipo de partición (teclee L para ver todos los tipos): 7

Se ha cambiado el tipo de la partición 'Linux' a 'HPFS/NTFS/exFAT'.

Orden (m para obtener ayuda): t
Número de partición (1,2,5-9, valor predeterminado 9): 8
Tipo de partición (teclee L para ver todos los tipos): l

 0  Vacía           24  DOS de NEC      81  Minix / Linux a bf  Solaris        
 1  FAT12           27  NTFS de WinRE o 82  Linux swap / So c1  DRDOS/sec (FAT-
 2  XENIX root      39  Plan 9          83  Linux           c4  DRDOS/sec (FAT-
 3  XENIX usr       3c  PartitionMagic  84  OS/2 oculto o h c6  DRDOS/sec (FAT-
 4  FAT16 <32M      40  Venix 80286     85  Linux extendida c7  Syrinx         
 5  Extendida       41  PPC PReP Boot   86  Conjunto de vol da  Datos sin SF   
 6  FAT16           42  SFS             87  Conjunto de vol db  CP/M / CTOS / .
 7  HPFS/NTFS/exFAT 4d  QNX4.x          88  Linux plaintext de  Utilidad Dell  
 8  AIX             4e  QNX4.x segunda  8e  Linux LVM       df  BootIt         
 9  AIX arrancable  4f  QNX4.x tercera  93  Amoeba          e1  DOS access     
 a  Gestor de arran 50  OnTrack DM      94  Amoeba BBT      e3  DOS R/O        
 b  W95 FAT32       51  OnTrack DM6 Aux 9f  BSD/OS          e4  SpeedStor      
 c  W95 FAT32 (LBA) 52  CP/M            a0  Hibernación de  ea  alineamiento Ru
 e  W95 FAT16 (LBA) 53  OnTrack DM6 Aux a5  FreeBSD         eb  BeOS fs        
 f  W95 Ext'd (LBA) 54  OnTrackDM6      a6  OpenBSD         ee  GPT            
10  OPUS            55  EZ-Drive        a7  NeXTSTEP        ef  EFI (FAT-12/16/
11  FAT12 oculta    56  Golden Bow      a8  UFS de Darwin   f0  inicio Linux/PA
12  Compaq diagnost 5c  Priam Edisk     a9  NetBSD          f1  SpeedStor      
14  FAT16 oculta <3 61  SpeedStor       ab  arranque de Dar f4  SpeedStor      
16  FAT16 oculta    63  GNU HURD o SysV af  HFS / HFS+      f2  DOS secondary  
17  HPFS/NTFS ocult 64  Novell Netware  b7  BSDI fs         fb  VMFS de VMware 
18  SmartSleep de A 65  Novell Netware  b8  BSDI swap       fc  VMKCORE de VMwa
1b  FAT32 de W95 oc 70  DiskSecure Mult bb  Boot Wizard hid fd  Linux raid auto
1c  FAT32 de W95 (L 75  PC/IX           bc  Acronis FAT32 L fe  LANstep        
1e  FAT16 de W95 (L 80  Minix antiguo   be  arranque de Sol ff  BBT            
Tipo de partición (teclee L para ver todos los tipos): b 

Se ha cambiado el tipo de la partición 'Linux' a 'W95 FAT32'.

Orden (m para obtener ayuda): t
Número de partición (1,2,5-9, valor predeterminado 9): 9
Tipo de partición (teclee L para ver todos los tipos): l

 0  Vacía           24  DOS de NEC      81  Minix / Linux a bf  Solaris        
 1  FAT12           27  NTFS de WinRE o 82  Linux swap / So c1  DRDOS/sec (FAT-
 2  XENIX root      39  Plan 9          83  Linux           c4  DRDOS/sec (FAT-
 3  XENIX usr       3c  PartitionMagic  84  OS/2 oculto o h c6  DRDOS/sec (FAT-
 4  FAT16 <32M      40  Venix 80286     85  Linux extendida c7  Syrinx         
 5  Extendida       41  PPC PReP Boot   86  Conjunto de vol da  Datos sin SF   
 6  FAT16           42  SFS             87  Conjunto de vol db  CP/M / CTOS / .
 7  HPFS/NTFS/exFAT 4d  QNX4.x          88  Linux plaintext de  Utilidad Dell  
 8  AIX             4e  QNX4.x segunda  8e  Linux LVM       df  BootIt         
 9  AIX arrancable  4f  QNX4.x tercera  93  Amoeba          e1  DOS access     
 a  Gestor de arran 50  OnTrack DM      94  Amoeba BBT      e3  DOS R/O        
 b  W95 FAT32       51  OnTrack DM6 Aux 9f  BSD/OS          e4  SpeedStor      
 c  W95 FAT32 (LBA) 52  CP/M            a0  Hibernación de  ea  alineamiento Ru
 e  W95 FAT16 (LBA) 53  OnTrack DM6 Aux a5  FreeBSD         eb  BeOS fs        
 f  W95 Ext'd (LBA) 54  OnTrackDM6      a6  OpenBSD         ee  GPT            
10  OPUS            55  EZ-Drive        a7  NeXTSTEP        ef  EFI (FAT-12/16/
11  FAT12 oculta    56  Golden Bow      a8  UFS de Darwin   f0  inicio Linux/PA
12  Compaq diagnost 5c  Priam Edisk     a9  NetBSD          f1  SpeedStor      
14  FAT16 oculta <3 61  SpeedStor       ab  arranque de Dar f4  SpeedStor      
16  FAT16 oculta    63  GNU HURD o SysV af  HFS / HFS+      f2  DOS secondary  
17  HPFS/NTFS ocult 64  Novell Netware  b7  BSDI fs         fb  VMFS de VMware 
18  SmartSleep de A 65  Novell Netware  b8  BSDI swap       fc  VMKCORE de VMwa
1b  FAT32 de W95 oc 70  DiskSecure Mult bb  Boot Wizard hid fd  Linux raid auto
1c  FAT32 de W95 (L 75  PC/IX           bc  Acronis FAT32 L fe  LANstep        
1e  FAT16 de W95 (L 80  Minix antiguo   be  arranque de Sol ff  BBT            
Tipo de partición (teclee L para ver todos los tipos): 82

Se ha cambiado el tipo de la partición 'Linux' a 'Linux swap / Solaris'.

Orden (m para obtener ayuda): p
Disco /dev/sdb: 1 GiB, 1073741824 bytes, 2097152 sectores
Unidades: sectores de 1 * 512 = 512 bytes
Tamaño de sector (lógico/físico): 512 bytes / 512 bytes
Tamaño de E/S (mínimo/óptimo): 512 bytes / 512 bytes
Tipo de etiqueta de disco: dos
Identificador del disco: 0x2744f900

Disposit.  Inicio Comienzo   Final Sectores Tamaño Id Tipo
/dev/sdb1             2048  309247   307200   150M 83 Linux
/dev/sdb2           309248 2097151  1787904   873M  5 Extendida
/dev/sdb5           311296  669695   358400   175M 83 Linux
/dev/sdb6           671744 1030143   358400   175M 83 Linux
/dev/sdb7          1032192 1390591   358400   175M  7 HPFS/NTFS/exFAT
/dev/sdb8          1392640 1751039   358400   175M  b W95 FAT32
/dev/sdb9          1753088 2097151   344064   168M 82 Linux swap / Solaris

Orden (m para obtener ayuda): w
Se ha modificado la tabla de particiones.
Llamando a ioctl() para volver a leer la tabla de particiones.
Se están sincronizando los discos.

root@debian:~# 
~~~


Formateo de las distintas particiones.
~~~
root@debian:~# mkfs.ext4 /dev/sdb1
mke2fs 1.43.4 (31-Jan-2017)
Se está creando un sistema de ficheros con 153600 bloques de 1k y 38456 nodos-i
UUID del sistema de ficheros: 8f286382-7d21-4bfe-bad7-3892ae70f074
Respaldo del superbloque guardado en los bloques: 
	8193, 24577, 40961, 57345, 73729

Reservando las tablas de grupo: hecho                           
Escribiendo las tablas de nodos-i: hecho                           
Creando el fichero de transacciones (4096 bloques): hecho
Escribiendo superbloques y la información contable del sistema de ficheros: hecho

root@debian:~# mkfs.ext4 /dev/sdb5
mke2fs 1.43.4 (31-Jan-2017)
Se está creando un sistema de ficheros con 179200 bloques de 1k y 44880 nodos-i
UUID del sistema de ficheros: bebf8bb5-ce05-45ab-9ced-f5f6eade1c23
Respaldo del superbloque guardado en los bloques: 
	8193, 24577, 40961, 57345, 73729

Reservando las tablas de grupo: hecho                           
Escribiendo las tablas de nodos-i: hecho                           
Creando el fichero de transacciones (4096 bloques): hecho
Escribiendo superbloques y la información contable del sistema de ficheros: hecho

root@debian:~# mkfs.ext4 /dev/sdb6
mke2fs 1.43.4 (31-Jan-2017)
Se está creando un sistema de ficheros con 179200 bloques de 1k y 44880 nodos-i
UUID del sistema de ficheros: e1f4a759-7d3f-4322-8728-acca96b31d5f
Respaldo del superbloque guardado en los bloques: 
	8193, 24577, 40961, 57345, 73729

Reservando las tablas de grupo: hecho                           
Escribiendo las tablas de nodos-i: hecho                           
Creando el fichero de transacciones (4096 bloques): hecho
Escribiendo superbloques y la información contable del sistema de ficheros: hecho

root@debian:~# mkfs.ntfs /dev/sdb7
Cluster size has been automatically set to 4096 bytes.
Initializing device with zeroes: 100% - Done.
Creating NTFS volume structures.
mkntfs completed successfully. Have a nice day.

root@debian:~# mkfs.vfat /dev/sdb8
mkfs.fat 4.1 (2017-01-24)

root@debian:~# mkswap /dev/sdb9
Configurando espacio de intercambio versión 1, tamaño = 168 MiB (176156672 bytes)
sin etiqueta, UUID=57037336-53c7-42dc-b55b-85a28a218e44

root@debian:~# lsblk -f
NAME   FSTYPE LABEL UUID                                 MOUNTPOINT
sda                                                      
├─sda1 ext4         9bb748be-c081-4450-8a0e-51903495fc92 /
├─sda2                                                   
└─sda5 swap         bff0697e-82c1-4182-bd1c-cac74dd0e016 [SWAP]
sdb                                                      
├─sdb1 ext4         8f286382-7d21-4bfe-bad7-3892ae70f074 
├─sdb2                                                   
├─sdb5 ext4         bebf8bb5-ce05-45ab-9ced-f5f6eade1c23 
├─sdb6 ext4         e1f4a759-7d3f-4322-8728-acca96b31d5f 
├─sdb7 ntfs         0D8AADC91FEF15E1                     
├─sdb8 vfat         D1D9-7AED                            
└─sdb9 swap         57037336-53c7-42dc-b55b-85a28a218e44                                                    
sr0                                                      
root@debian:~# 
~~~


## Segundo esquema.
- Disco duro: 1 GB
- Partición primaria: 200 MB
- Partición primaria: 100 MB
- Hueco: 500 MB
- Partición extendida.

Ejecutamos **fdisk** indicando el disco que queremos formatear.
~~~
root@debian:~# fdisk /dev/sdc

Bienvenido a fdisk (util-linux 2.29.2).
Los cambios solo permanecerán en la memoria, hasta que decida escribirlos.
Tenga cuidado antes de utilizar la orden de escritura.

El dispositivo no contiene una tabla de particiones reconocida.
Se ha creado una nueva etiqueta de disco DOS con el identificador de disco 0xea6ca7f6.

Orden (m para obtener ayuda): 
~~~


Creación de las distintas particiones primarias.
~~~
Orden (m para obtener ayuda): n
Tipo de partición
   p   primaria (0 primaria(s), 0 extendida(s), 4 libre(s))
   e   extendida (contenedor para particiones lógicas)
Seleccionar (valor predeterminado p): p
Número de partición (1-4, valor predeterminado 1): 
Primer sector (2048-2097151, valor predeterminado 2048): 
Último sector, +sectores o +tamaño{K,M,G,T,P} (2048-2097151, valor predeterminado 2097151): +200M

Crea una nueva partición 1 de tipo 'Linux' y de tamaño 200 MiB.

Orden (m para obtener ayuda): n
Tipo de partición
   p   primaria (1 primaria(s), 0 extendida(s), 3 libre(s))
   e   extendida (contenedor para particiones lógicas)
Seleccionar (valor predeterminado p): p
Número de partición (2-4, valor predeterminado 2): 
Primer sector (411648-2097151, valor predeterminado 411648): 
Último sector, +sectores o +tamaño{K,M,G,T,P} (411648-2097151, valor predeterminado 2097151): +100M

Crea una nueva partición 2 de tipo 'Linux' y de tamaño 100 MiB.

Orden (m para obtener ayuda): p
Disco /dev/sdc: 1 GiB, 1073741824 bytes, 2097152 sectores
Unidades: sectores de 1 * 512 = 512 bytes
Tamaño de sector (lógico/físico): 512 bytes / 512 bytes
Tamaño de E/S (mínimo/óptimo): 512 bytes / 512 bytes
Tipo de etiqueta de disco: dos
Identificador del disco: 0xea6ca7f6

Disposit.  Inicio Comienzo  Final Sectores Tamaño Id Tipo
/dev/sdc1             2048 411647   409600   200M 83 Linux
/dev/sdc2           411648 616447   204800   100M 83 Linux

Orden (m para obtener ayuda): w
Se ha modificado la tabla de particiones.
Llamando a ioctl() para volver a leer la tabla de particiones.
Se están sincronizando los discos.

root@debian:~# 
~~~


Creación de la partición swap.
~~~
Orden (m para obtener ayuda): n
Tipo de partición
   p   primaria (2 primaria(s), 0 extendida(s), 2 libre(s))
   e   extendida (contenedor para particiones lógicas)
Seleccionar (valor predeterminado p): e
Número de partición (3,4, valor predeterminado 3): 
Primer sector (616448-2097151, valor predeterminado 616448): 1640448
Último sector, +sectores o +tamaño{K,M,G,T,P} (1640448-2097151, valor predeterminado 2097151): 

Crea una nueva partición 3 de tipo 'Extended' y de tamaño 223 MiB.

Orden (m para obtener ayuda): t
Número de partición (1-3, valor predeterminado 3): 3
Tipo de partición (teclee L para ver todos los tipos): l

 0  Vacía           24  DOS de NEC      81  Minix / Linux a bf  Solaris        
 1  FAT12           27  NTFS de WinRE o 82  Linux swap / So c1  DRDOS/sec (FAT-
 2  XENIX root      39  Plan 9          83  Linux           c4  DRDOS/sec (FAT-
 3  XENIX usr       3c  PartitionMagic  84  OS/2 oculto o h c6  DRDOS/sec (FAT-
 4  FAT16 <32M      40  Venix 80286     85  Linux extendida c7  Syrinx         
 5  Extendida       41  PPC PReP Boot   86  Conjunto de vol da  Datos sin SF   
 6  FAT16           42  SFS             87  Conjunto de vol db  CP/M / CTOS / .
 7  HPFS/NTFS/exFAT 4d  QNX4.x          88  Linux plaintext de  Utilidad Dell  
 8  AIX             4e  QNX4.x segunda  8e  Linux LVM       df  BootIt         
 9  AIX arrancable  4f  QNX4.x tercera  93  Amoeba          e1  DOS access     
 a  Gestor de arran 50  OnTrack DM      94  Amoeba BBT      e3  DOS R/O        
 b  W95 FAT32       51  OnTrack DM6 Aux 9f  BSD/OS          e4  SpeedStor      
 c  W95 FAT32 (LBA) 52  CP/M            a0  Hibernación de  ea  alineamiento Ru
 e  W95 FAT16 (LBA) 53  OnTrack DM6 Aux a5  FreeBSD         eb  BeOS fs        
 f  W95 Ext'd (LBA) 54  OnTrackDM6      a6  OpenBSD         ee  GPT            
10  OPUS            55  EZ-Drive        a7  NeXTSTEP        ef  EFI (FAT-12/16/
11  FAT12 oculta    56  Golden Bow      a8  UFS de Darwin   f0  inicio Linux/PA
12  Compaq diagnost 5c  Priam Edisk     a9  NetBSD          f1  SpeedStor      
14  FAT16 oculta <3 61  SpeedStor       ab  arranque de Dar f4  SpeedStor      
16  FAT16 oculta    63  GNU HURD o SysV af  HFS / HFS+      f2  DOS secondary  
17  HPFS/NTFS ocult 64  Novell Netware  b7  BSDI fs         fb  VMFS de VMware 
18  SmartSleep de A 65  Novell Netware  b8  BSDI swap       fc  VMKCORE de VMwa
1b  FAT32 de W95 oc 70  DiskSecure Mult bb  Boot Wizard hid fd  Linux raid auto
1c  FAT32 de W95 (L 75  PC/IX           bc  Acronis FAT32 L fe  LANstep        
1e  FAT16 de W95 (L 80  Minix antiguo   be  arranque de Sol ff  BBT            
Tipo de partición (teclee L para ver todos los tipos): 82

Se ha cambiado el tipo de la partición 'Extended' a 'Linux swap / Solaris'.

Orden (m para obtener ayuda): p
Disco /dev/sdc: 1 GiB, 1073741824 bytes, 2097152 sectores
Unidades: sectores de 1 * 512 = 512 bytes
Tamaño de sector (lógico/físico): 512 bytes / 512 bytes
Tamaño de E/S (mínimo/óptimo): 512 bytes / 512 bytes
Tipo de etiqueta de disco: dos
Identificador del disco: 0xea6ca7f6

Disposit.  Inicio Comienzo   Final Sectores Tamaño Id Tipo
/dev/sdc1             2048  411647   409600   200M 83 Linux
/dev/sdc2           411648  616447   204800   100M 83 Linux
/dev/sdc3          1640448 2097151   456704   223M 82 Linux swap / Solaris

Orden (m para obtener ayuda): w
Se ha modificado la tabla de particiones.
Llamando a ioctl() para volver a leer la tabla de particiones.
Se están sincronizando los discos.

root@debian:~# 
~~~


Formateo de las particiones.
~~~
root@debian:~# mkfs.ext4 /dev/sdc1
mke2fs 1.43.4 (31-Jan-2017)
Se está creando un sistema de ficheros con 204800 bloques de 1k y 51200 nodos-i
UUID del sistema de ficheros: ac19ca13-5d3d-432f-8320-7e2a94a1e026
Respaldo del superbloque guardado en los bloques: 
	8193, 24577, 40961, 57345, 73729

Reservando las tablas de grupo: hecho                           
Escribiendo las tablas de nodos-i: hecho                           
Creando el fichero de transacciones (4096 bloques): hecho
Escribiendo superbloques y la información contable del sistema de ficheros: hecho

root@debian:~# mkfs.ext4 /dev/sdc2
mke2fs 1.43.4 (31-Jan-2017)
Se está creando un sistema de ficheros con 102400 bloques de 1k y 25688 nodos-i
UUID del sistema de ficheros: c63561a6-ae76-48bd-b4d7-0c74fd480373
Respaldo del superbloque guardado en los bloques: 
	8193, 24577, 40961, 57345, 73729

Reservando las tablas de grupo: hecho                           
Escribiendo las tablas de nodos-i: hecho                           
Creando el fichero de transacciones (4096 bloques): hecho
Escribiendo superbloques y la información contable del sistema de ficheros: hecho

root@debian:~# mkswap /dev/sdc3
Configurando espacio de intercambio versión 1, tamaño = 223 MiB (233828352 bytes)
sin etiqueta, UUID=a520fd3d-50e9-43d2-b548-c91e91093f3b
root@debian:~# lsblk -f
NAME   FSTYPE LABEL UUID                                 MOUNTPOINT
sda                                                      
├─sda1 ext4         9bb748be-c081-4450-8a0e-51903495fc92 /
├─sda2                                                   
└─sda5 swap         bff0697e-82c1-4182-bd1c-cac74dd0e016 [SWAP]
sdb                                                      
├─sdb1 ext4         8f286382-7d21-4bfe-bad7-3892ae70f074 
├─sdb2                                                   
├─sdb5 ext4         bebf8bb5-ce05-45ab-9ced-f5f6eade1c23 
├─sdb6 ext4         e1f4a759-7d3f-4322-8728-acca96b31d5f 
├─sdb7 ntfs         0D8AADC91FEF15E1                     
├─sdb8 vfat         D1D9-7AED                            
└─sdb9 swap         57037336-53c7-42dc-b55b-85a28a218e44    
sdc                                                      
├─sdc1 ext4         5a534de5-96d1-4a5a-ad5e-2beff77db144 
├─sdc2 ext4         caad7d21-c43c-4c24-9a36-171435356ef1 
└─sdc3 swap         363332a4-15c6-4e12-a10e-fe4439ad65eb                                             
sr0                                                      
root@debian:~# 
~~~