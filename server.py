import socket, threading, hashlib
from _thread import *

print_lock = threading.Lock()


def threaded(c):
    while True:

        data = c.recv(1024)
        print (data)
        if not data:
            print("disconnected")
            print_lock.release()
            break

        if(data=="1".encode()):
            file = open ("./archivos/1", "rb")
            foo = file.read(1024)
            while(foo):
                c.send(foo)
                foo = file.read(1024)

        if(data=="2".encode()):
            file = open ("./archivos/2", "rb")
            foo = file.read(1024)
            while(foo):
                c.send(foo)
                foo = file.read(1024)
        else:
            response="no such file"
            sender=response.encode()
            c.send(sender)

        c.close()

def main():
    print("Start")
    host="127.0.0.1"
    port=8080

    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    print("connected socket on port ",port)
    sock.listen(25)
    print("listening on port ",port)

    while True:

        c, address = sock.accept()

        print_lock.acquire()
        print('Connected to :', address[0], ':', address[1])
        start_new_thread(threaded, (c,))
    sock.close()

#robado de stack overflow
def generateHash(file):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

main()
