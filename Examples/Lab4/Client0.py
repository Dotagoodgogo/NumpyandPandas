import pickle
import socket
from Graph import Graph
from Business import Business
class Client0:
    def __init__(self):
        self.I=Business()
        self.G=Graph()
        self.clist=[]

    def client_program(self):
        print("[Client]Send any message to receive data")

        host = socket.gethostname()
        port = 5000

        client_socket = socket.socket()
        client_socket.connect((host, port))

        message = input(" -> ")
        client_socket.send(message.encode())

        while message.lower().strip() != 'bye':


                data = client_socket.recv(1024)
                self.clist=pickle.loads(data)

                print('[Client]Received from server: ' , self.clist)
                self.Graph()
                print("[Client]Data recevied.Closing the window.")
                break
        client_socket.close()







    def Graph(self):
        self.G.DataProc(self.clist)
        self.G.XY_plotbyC()



if __name__ == '__main__':
    p=Client0()
    p.client_program()
