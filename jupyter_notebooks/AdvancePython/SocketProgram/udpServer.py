import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("Server started")
    while True:
        data, addr = s.recvfrom(1024)
        print("message from: "+ str(addr))
        data=str(data.decode())
        print("from connected user: "+ data )
        print("sending: "+ data.upper())
        s.sendto(data.upper().encode(),addr)
    s.close()

if __name__ == '__main__':
    Main()
