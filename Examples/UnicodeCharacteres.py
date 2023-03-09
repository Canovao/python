# Unicode is used to represent any character of any language of any country

# Always encode to UTF-8, it's just better
# Always use the latest python version, it's updated for unicode characteres

# ord() -> Returns ASCII code of an charactere
print(ord('H'))
print(ord('G'))
print(ord('6'))
print(ord('\n'))

#Example with An HTTP Request in Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    mystring = data.decode()
    print(data)
mysock.close()