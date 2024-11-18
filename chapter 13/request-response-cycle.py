import socket

#request response cycle activity
#this line of code is what make the connection of our code to communicate with the server or internet
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#this line of code is similar to dialing a phone number with a phone extension
mysock.connect(('data.pr4e.org', 80))

#this line of code is what we are trying to request to the phone number that we dialed. we need .encode() so it can be readable
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#now we send the request that we made
mysock.send(cmd)

#now this while loop is like reading the data that we requested and then decoding it
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()