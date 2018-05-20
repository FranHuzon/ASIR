####  Configura todo lo necesario para que los dos dominios estén operativos. Se deberán configurar los clientes para que puedan iniciar sesión en sus respectivos dominios. Explica de forma detallada todos y cada uno de los pasos necesarios para tal fin.


#### Pasos:
 - Paso 1. Creación del dominio.
 - Paso 2. Creación de los usuarios.
 - Paso 3. Añadir los clientes al dominio.


##### Paso 1.
Accedemos a **Add roles and features** a través de **Manage**, en la pestaña Server Roles marcamos **Active Directory Domain Services**, confirmamos los cambios y comenzamos la instalación. Una vez instalado el rol accedemos a las notificaciones y hacemos click en **Promote this server to a domain controller**, en la pestaña **Deployment Configuration** marcamos la opción **Add a new forest** e indicamos el nombre del dominio.


##### Paso 2.
Accedemos a **Active Directory Users and Computers** a través de **Tools**,


#### Necesitamos acceder a los recursos compartidos del otro dominio, ¿qué debemos configurar entre los dominios. Explica de forma detallada todos y cada uno de los pasos necesarios. ¿Qué ocurriría si se configura únicamente una relación de confianza unidireccional entre los dos dominios?. Explícalo detalladamente. El dominio PrimerApellido.local, comparte la carpeta PrimerApellidoComparte, para que los usuarios del dominio de PrimerApellido.local., puedan acceder a su lectura. Sería deseable que los usuarios de SegundoApellido.local pudieran también acceder, ¿qué deberías configurar?


#### Pasos:
 - Paso 1. Desactivar el firewall de Windows.
 - Paso 2. Modificar los reenviadores condicionales.
 - Paso 3. Crear la relación de confianza bidireccional.
 - Paso 4. Crear la carpeta compartida.
 - Paso 5. Acceder al recurso compartido.


#### Supongamos que el administrador del dominio PrimerApellido.local, necesitara administrar su dominio, y además el dominio SegundoApellido.local. ¿Qué necesitamos configurar para que pueda administrar ambos dominios.


#### Pasos:
 - Paso 1. Añadir el segundo dominio como nodo de navegación.


#### Sobre la relación de confianza entre PrimerApellido.local y SegundoApellido.local, modificala para que la autentificación sea selectiva. ¿Qué debes configurar para que los usuarios del apartado 3 puedan seguir accediendo a PrimerApellidoComparte?. Explica la diferencia entre autenticación selectiva y autenticación en todo el dominio. 


#### Pasos:
 - Paso 1: Modificar la relación de confianza existente.
