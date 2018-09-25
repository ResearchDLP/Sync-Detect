import socket
from time import sleep
import datetime



class Client:

    def __init__(self, data):
        ip = '192.168.8.103'
        port = 60000  # Reserve a port for your service.
        s = socket.socket()  # Create a socket object
        host, rest, ipp = socket.gethostbyaddr(ip)  # Get local machine name
        # host = socket.gethostname()

        s.connect((host, port))

        print('info sending done')
        s.send(str(data).encode("utf-8"))
        sleep(1)

        filepath = data['evidence']['filepath']
        f = open(filepath, 'rb')
        l = f.read(1024)
        print(l)
        while l:
            s.send(l)
            print('Sent ', repr(l))
            l = f.read(1024)
        f.close()

        print('Done sending')
        s.close()



timestamp = str(datetime.datetime.now()).split('.')[0]

# cloud analyser
data1 = {"moduleType": "email", "alertDetails": {"up_time": "", "up_link": "", "severity": "", "policy_name": ""}, "hostdetails":  {"hostname": "", "os": "", "version": "", "details": "", "host_user":""}, "evidence": {"filename": "", "filepath": ""}, "timestamp": timestamp}


client = Client(data1)
