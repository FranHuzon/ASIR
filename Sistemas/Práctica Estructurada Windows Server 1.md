###  Configura todo lo necesario para que los dos dominios estén operativos. Se deberán configurar los clientes para que puedan iniciar sesión en sus respectivos dominios. Explica de forma detallada todos y cada uno de los pasos necesarios para tal fin.


#### Pasos:
 - Paso 1. Creación del dominio.
 - Paso 2. Creación de los usuarios.
 - Paso 3. Modificar el servidor DNS de los clientes.
 - Paso 4. Añadir los clientes al dominio.


***Paso 1:***
Accedemos a **Add roles and features** a través de **Manage**, en la pestaña Server Roles marcamos **Active Directory Domain Services**, confirmamos los cambios y comenzamos la instalación. Una vez instalado el rol accedemos a las notificaciones y hacemos click en **Promote this server to a domain controller**, en la pestaña **Deployment Configuration** marcamos la opción **Add a new forest** e indicamos el nombre del dominio (*garcia.local/munoz.local*).


***Paso 2:***
Accedemos a **Active Directory Users and Computers** a través de **Tools**, desplegamos nuestro dominio (*garcia.local/munoz.local*), hacemos click derecho en **Users** y en el desplagable **New** seleccionamos **User**, por ultimo indicamos el nombre de usuario (*CLIENTgarcia/CLIENTmunoz*) así como su contraseña.


***Paso 3:***
Desde **Powershell** ejecutamos el comando ``sconfig``, una vez en el menú seleccionamos la opción 8 (**Network Settings**), indicamos la interfaz que deseamos modificar a través de su número (**#**), por último seleccionamos la opción 2 (**Set DNS Server**) e indicamos la dirección IP del controlador de dominio (*DCgarcia/DCmunoz*).


***Paso 4:***
Desde **Powershell** ejecutamos el comando ``sconfig``, una vez en el menú seleccionamos la opción 1 (**Domain/Workgroup**), elegimos la opción D (**Domain**), indicamos el dominio al que queremos unirnos (*garcia.local/munoz.local*)y nos logeamos con el usuario creado previamente (*CLIENTgarcia/CLIENTmunoz*).


### Necesitamos acceder a los recursos compartidos del otro dominio, ¿qué debemos configurar entre los dominios. Explica de forma detallada todos y cada uno de los pasos necesarios. ¿Qué ocurriría si se configura únicamente una relación de confianza unidireccional entre los dos dominios?. Explícalo detalladamente. El dominio PrimerApellido.local, comparte la carpeta PrimerApellidoComparte, para que los usuarios del dominio de PrimerApellido.local., puedan acceder a su lectura. Sería deseable que los usuarios de SegundoApellido.local pudieran también acceder, ¿qué deberías configurar?


#### Pasos:
 - Paso 1. Desactivar el firewall de Windows.
 - Paso 2. Modificar los reenviadores condicionales.
 - Paso 3. Crear la relación de confianza bidireccional.
 - Paso 4. Compartir la carpeta con el otro dominio.


***Paso 1:***
Desde **Powershell** ejecutamos el comando ``netsh advfirewall set allprofiles state off``.


***Paso 2:***
Accedemos a **DNS** a través de **Tools**, seleccionamos la pestaña **Conditional Forwarders**, hacemos click derecho y entramos en **New Conditional Forwarder**, por último indicamos el nombre del segundo dominio (*munoz.local*), la dirección IP de su controlador de dominio y marcamos la opción **Store this conditional forwarder...**.
 
 
***Paso 3:***
Accedemos a **Active Directory Domains and Trusts** a través de **Tools**, hacemos click derecho y entramos en **Properties**,en la pestaña **Trusts** seleccionamos **New Trust**, indicamos el nombre del dominio con el que queremos hacer la relación (*munoz.local*), y marcamos las siguientes opciones; **Forest Trust**, **Two-way trust**, **Both this domain and the specified domain** y **Forest-wide authentication**.
 
 
***Paso 4:***
Para compartir la carpeta con el otro dominio, en la opción **Location** debemos indicar el nombre del segundo dominio (*munoz.local*) y añadir el grupo **Domain Users** de dicho dominio.


### Supongamos que el administrador del dominio PrimerApellido.local, necesitara administrar su dominio, y además el dominio SegundoApellido.local. ¿Qué necesitamos configurar para que pueda administrar ambos dominios.


#### Pasos:
 - Paso 1. Añadir el segundo dominio como nodo de navegación.


***Paso 1:***
Accedemos a **Active Directory Administrative Center** a través de **Administrative Tools**, en **Manage** seleccionamos **Add navigation Nodes**, hacemos click en **Connect to other domains**, indicamos el nombre del segundo dominio (*munoz.local*) y añadimos el contenedor del dominio (*munoz*).


### Sobre la relación de confianza entre PrimerApellido.local y SegundoApellido.local, modificala para que la autentificación sea selectiva. ¿Qué debes configurar para que los usuarios del apartado 3 puedan seguir accediendo a PrimerApellidoComparte?. Explica la diferencia entre autenticación selectiva y autenticación en todo el dominio. 


#### Pasos:
 - Paso 1: Modificar la relación de confianza existente.
 
 
***Paso 1:***
Accedemos a **Active Directory Domains and Trusts** a través de **Tools**, hacemos click derecho y entramos en **Properties**,vamos a la pestaña **Trusts**, en el apartado **Incoming Trusts**, seleccionamos la relación con el otro dominio (*munoz.local*), entramos en **Properties** y en la pestaña **Authentication** mascamos la opción **Selective Authentication**.
