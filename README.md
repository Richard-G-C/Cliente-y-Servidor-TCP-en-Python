 Esenciales Git
Servidor TCP que interactúe con un cliente.
Este proyecto implementa un servidor y un cliente TCP en Python que se comunican a través del puerto 5000 en `localhost`.

 Instrucciones

 1. Requisitos
Asegúrate de tener Python instalado en tu máquina. Este código fue probado en Python 3.12.4

 2. Iniciar el Servidor
Ejecuta el siguiente comando en la terminal para iniciar el servidor:
python servidor.py
 3. Ejecutar el Cliente:
En la otra terminal
Ejecuta el cliente usando el siguiente comando:
python cliente.py
Esto iniciará el cliente y te pedirá que ingreses un mensaje.

Realizar Pruebas Manuales:

Prueba 1: Ingresa cualquier mensaje, como hola, en la terminal del cliente. Verás que el servidor responde con el mismo mensaje en mayúsculas (HOLA).
Prueba 2: Ingresa el mensaje DESCONEXION. Esto hará que el cliente envíe la señal de desconexión al servidor. El cliente se cerrará, y el servidor mostrará en su terminal que el cliente se ha desconectado.


