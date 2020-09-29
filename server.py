import socket, threading
from _thread import *

print_lock = threading.Lock()

def threaded(c):
    while True:

        data = c.recv(1024)
        if not data:
            print("disconnected")
            print_lock.release()
            break

        response="response "+str(data)
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
    sock.listen(5)
    print("listening on port ",port)

    while True:

        c, address = sock.accept()

        print_lock.acquire()
        print('Connected to :', address[0], ':', address[1])
        start_new_thread(threaded, (c,))
    sock.close()

main()
