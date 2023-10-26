import socket
def convert_interger():
    data = 1234
    print ("original: %s ==> Long Host Byte Order: %s, Network byte order: %s"
    %(data, socket.ntoh1(data), socket.hton1(data)))
    print ("Original: %s ==> Short host byte order: %s, Network by order: %s"
    %(data, socket.ntohs(data), socket.htons(data)))
if __name__ == '__main__':
    convert_interger()