import socket

url = "canova-games.web.app"
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url, 80))
#mysock.connect(("host", port))
cmd = f"GET https://{url} HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())