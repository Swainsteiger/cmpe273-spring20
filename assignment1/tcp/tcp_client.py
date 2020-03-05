import socket
import sys
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"


def send(id):
    delay = int(sys.argv[2])
    repeat_num = int(sys.argv[3])
    count = 1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    while count <= repeat_num:
        s.send(f"{id}:{MESSAGE}".encode())
        data = s.recv(BUFFER_SIZE)
        print("received data:", data.decode())
        count += 1
        time.sleep(delay)
    s.close()


def get_client_id():
    id = sys.argv[1]
    return id


if __name__ == "__main__":
    send(get_client_id())
