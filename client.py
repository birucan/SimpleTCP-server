import socket, os


def createSocket(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        print("Connection succesful with ",ip,":",port)
    except Exception as e:
        print("Unable to connect")
        raise

    #hola =open("./archivos/hola.txt", "rt")
    hola= "hola bb como estas el dia de hoy"
    hello =hola.encode()
    sock.send(hello)
    response = "non"

    while response == "non":
        response=sock.recv(4096)
        print(response)

    sock.close()



createSocket("localhost", 8080)
