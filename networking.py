import socket,pprint

def MyTcpClient():
    target_host = '0.0.0.0'
    target_port = 9999
    #target_host = 'www.google.com'
    #target_port = 80

    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the client
    client.connect((target_host, target_port))
    # send some data
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    # recieve some data
    response = client.recv(4096)
    pprint.pprint ( response )

#MyTcpClient()
def MyUDPClient():
    target_host = "127.0.0.1"
    target_port = 80
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # send some data
    client.sendto(b"AAABBBCCC",(target_host,target_port))
    #receive some dat
    data,addr = client.recvfrom(4096)
    print ( data,addr )

MyTcpClient()
