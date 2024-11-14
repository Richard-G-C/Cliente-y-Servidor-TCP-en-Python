import socket

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("localhost", 5000))
    servidor.listen(5)
    print("Servidor TCP esperando conexiones en el puerto 5000...")

    while True:
        conexion, direccion = servidor.accept()
        print(f"Conexión establecida con {direccion}")

        while True:
            mensaje = conexion.recv(1024).decode()
            if not mensaje:
                break
            print(f"Mensaje recibido: {mensaje}")

            if mensaje == "DESCONEXION":
                print("Cliente desconectado.")
                conexion.close()
                break
            else:
                respuesta = mensaje.upper()
                conexion.send(respuesta.encode())
                print(f"Respuesta enviada: {respuesta}")

if __name__ == "__main__":
    iniciar_servidor()





