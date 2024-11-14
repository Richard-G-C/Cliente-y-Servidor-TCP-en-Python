import socket

def iniciar_cliente():

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("localhost", 5000))

    while True:
       
        mensaje = input("Ingrese un mensaje (o 'DESCONEXION' para salir): ")
        
        cliente.send(mensaje.encode())

        if mensaje == "DESCONEXION":
            print("Desconectando del servidor...")
            cliente.close()
            break

        respuesta = cliente.recv(1024).decode()
        print(f"Respuesta del servidor: {respuesta}")

if __name__ == "__main__":
    iniciar_cliente()

