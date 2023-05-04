# Final Telematica

Los requerimentos de la ultima entrega en el curso de telematica piden crear 3 dockers distintos de la siguiente manera:

1. El primero consultara datos a la SIATA mediante la API correspondiente.
2. El segundo se encarga de tener una serie de usuarios y contraseñas funcionando como una DataBase.
3. El tercero se encarga de todo lo relacionado con el FrontEnd del proyecto. Este hace la validacion del usuario y la contraseña
ingresada en el docker de base de datos y presenta tanto el formulario de inicio de sesion, como la grafica de la SIATA una vez se inicio
satisfactoriamente sesion.

Algunas de las caracteristicas mas relevantes de los dockers son los puertos por donde corren.

1. API: http://localhost:5000/mostrar_estacionesnivel
2. DB: http://localhost:3000/database
3. FRONT: http://localhost:8080

En este repositorio se encuentran los archivos necesarios para montar todo lo anteriormente mencionado. Basta con ingresar a la instancia de AWS, ingresar a la carpeta llamada "Proyecto_Final" y ejecutar el archivo alli ubicado, llamado "script.sh".

Este script desplegara todo lo relacionado con imagenes y dockers, siguiendo la arquitectura que se tiene en el repositorio.

Realizado por: Andres Benjumea Reinoso y Juan Andres Porras Velez.
