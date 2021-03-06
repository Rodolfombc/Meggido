try:    import cPickle as pickle
except: import  pickle as pickle
import zlib

from _mm_constants import *

def packet_send(socket,protocol_and_udpaddress, data,compression): #E.g.: =(MM_TCP,None)
    if   compression ==  False: compression = 0
    elif compression ==   None: compression = 0
    elif compression ==   True: compression = 9
    elif compression == MM_MAX: compression = 9

    data_to_send = str(compression).encode() #length is now 1

    data_str = pickle.dumps(data)
    if compression != 0:
        data_str = zlib.compress(data_str,compression)

    length_str = str(len(data_str)).encode()
    data_to_send += (16-len(length_str))*b" "
    data_to_send += length_str #length is now 17
    data_to_send += data_str #length is now 17+len(data_str)

    try:
        if protocol_and_udpaddress[0] == MM_TCP:
            socket.sendall(data_to_send)
        else:
            if protocol_and_udpaddress[1] == None:
                socket.sendall(data_to_send)
            else:
                socket.sendto(data_to_send, protocol_and_udpaddress[1])
        return True
    except:
        return False
def packet_recv_tcp(socket):
    info = b""
    try:
        while len(info) < 17:
            got = socket.recv(17)
            if got == b"": raise "EOF" #goto except
            info += got
    except:
        return (None,False)
    if info == b"": return (None,False)

    compression = int(info[0:1])
    length = int(info[1:])

    data_str = b""
    try:
        while len(data_str) < length:
            got = socket.recv(length)
            if got == b"": raise "EOF" #goto except
            data_str += got
    except:
        return (None,False)
    if compression != 0:
        data_str = zlib.decompress(data_str)

    data = pickle.loads(data_str)
    
    return data,True
def packet_recv_udp(socket,max_packet_size):
    data_str,address = socket.recvfrom(max_packet_size)
    info = data_str[0:17]
    data_str = data_str[17:]

    compression = int(info[0:1])
    length = int(info[1:])

    if compression != 0:
        data_str = zlib.decompress(data_str)
    
    data = pickle.loads(data_str)
    
    return data,address
