### Configura todo lo necesario para que el Dominio empresa, dominio subordinado de PrimerApellido, quede integrado dentro del bosque iniciado con PrimerApellido.local.


#### Pasos:
 - Paso 1. Instalación del rol de Active Directory.
 - Paso 2. Configuración de los servidores DNS.
 - Paso 3. Creación del dominio empresa.garcia.local.


***Paso 1:***
Accedemos a **Add roles and features** a través de **Manage**, en la pestaña Server Roles marcamos **Active Directory Domain Services**, confirmamos los cambios y comenzamos la instalación.


***Paso 2:***
Desde **Powershell** ejecutamos el comando ``sconfig``, una vez en el menú seleccionamos la opción 8 (**Network Settings**), indicamos la interfaz que deseamos modificar a través de su número (**#**), por último seleccionamos la opción 2 (**Set DNS Server**) e indicamos la dirección IP del controlador de dominio (*DCgarcia*).


***Paso 3:***
Una vez instalado el rol accedemos a las notificaciones y hacemos click en **Promote this server to a domain controller**, en la pestaña **Deployment Configuration** marcamos la opción **Add a domain to an existing forest**, en **parent domain name** indicamos el nombre del dominio principal (*garcia.local*), en **new domain name** indicamos el nombre del dominio secundario (*empresa*), por último indicamos los credenciales para poder crear el dominio (*GARCIA\Administrator*).


***Notas:***
Para que *DCgarcia* puede administrar los dominios *garcia.local* y *empresa.garcia.local* mientras que *DCempresa* solo puede administrar el dominio *empresa.garcia.local*, haremos lo siguiente:


***Paso 1: Modificar los reenviadores condicionales.***
Accedemos a **DNS** a través de **Tools**, seleccionamos la pestaña **Conditional Forwarders**, hacemos click derecho y entramos en **New Conditional Forwarder**, por último indicamos el nombre del dominio secundario (*empresa.garcia.local*), la dirección IP de su controlador de dominio y marcamos la opción **Store this conditional forwarder...**.


***Paso 2: Añadir DCempresa a la lista de servidores de DCgarcia.***
Accedemos a **Add servers** a través de **Manage**, en **Location** indicamos el nombre del dominio secundario (*empresa.garcia.local*), hacemos click en **Find now** y añadimos el controlar de dominio de dicho dominio (*DCempresa*).


### Crea una unidad organizativa en PrimerApellido.local llamada MiEmpresa, dentro de ella crea otra unidad organizativa llamada prueba. En ella introduce a usuarioPrimerApellido. Aplica sobre la unidad organizativa prueba directivas de seguridad para que usuarioPrimerApellido tenga limitado el acceso a determinadas partes de su sistema operativo. Justifica las decisiones adoptadas.


#### Pasos:
 - Paso 1. Crear ambas unidades organizativas.
 - Paso 2. Añadir el usuario deseado a la unidad organizativa.


***Paso 1:***
Accedemos a **Active Directory Users and Computers** a través de **Tools**, hacemos click derecho en el dominio (*garcia.local*), en **New** seleccionamos **Organizational Unit** e indicamos el nombre (*MiEmpresa*) por último hacemos click derecho en la unidad organizativa y creamos otra dentro de esta (*prueba*).


***Paso 2:***
Accedemos a **Active Directory Users and Computers** a través de **Tools**, desplegamos nuestro dominio (*garcia.local*), entramos en **Users**, hacemos click derecho en el usuario que deseemos (*CLIENTgarcia*), entramos en **Move** y seleccionamos la unidad organizativa creada anteriormente (*prueba*).