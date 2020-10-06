import socket, os, hashlib, time


def createSocket(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        print("Connection succesful with ",ip,":",port)
    except Exception as e:
        print("Unable to connect")
        raise

    hola= input('seleccione archivo 1 o 2:')
    hello =hola.encode()
    sock.send(hello)

    file= sock.recv(1024)
    fileLocal= open(hola, "wb")

    ts = time.time()
    while (file):
        fileLocal.write(file)
        file = sock.recv(1024)

    ts= time.time() - ts
    print("archivo recibido en ", ts, " milisegundos")
    sock.close()

#robado de stack overflow
def generateHash(file):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

createSocket("localhost", 8080)
