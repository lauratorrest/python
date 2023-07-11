import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Iniciando Servidor en  {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('esperando por conexion')
    connection, client_address = sock.accept()
    try:
        print('conexion recibida desde ', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('Datos recibidos del Cliente {!r}'.format(data))
            if data:
                print('Enviando datos de regreso al Cliente')
                connection.sendall(data)
            else:
                print('no se enviaron datos del Cliente', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()