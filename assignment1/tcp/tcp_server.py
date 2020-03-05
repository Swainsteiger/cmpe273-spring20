import socket
from threading import Thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024


def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(10)

    print(f'Server at port:{TCP_PORT}')

    while True:
        conn, addr = s.accept()
        Thread(target=client_thread, args=(conn, addr)).start()


def client_thread(conn,addr):
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            print(f'End of data transmission from client[IP:{addr[0]},Port:{addr[1]}]')
            conn.close()
            break
        print(f"received data:{data.decode()}")
        conn.send("pong".encode())


if __name__ == "__main__":
    listen_forever()
