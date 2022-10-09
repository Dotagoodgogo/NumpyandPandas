import pickle
import socket
from Graph import Graph
from User_Layer import User
from Business import Business


class Server0:
    def __init__(self):
        self.I=Business()

    def processData(self):
        self.I.DataCenter()





    def server_program(self):

        host = socket.gethostname()
        port = 5000

        server_socket = socket.socket()
        server_socket.bind((host, port))
        print("[Server]Server is online")
        print("[Server]User selected ",self.I.Country,". Sending data to client")


        server_socket.listen(2)
        conn, address = server_socket.accept()
        print("[Server]Connection from: " + str(address))
        Connected= True
        while Connected:

            data = conn.recv(1024).decode()

            if not data:

                break
            print("[Server]from connected user: ", str(data))
            data=pickle.dumps(self.I.Cou)
            conn.send(data)
            print("[Server]Data transform completed.")

            '''
            else:

                print("from connected user: " , str(data))

                data = input(' -> ')
                conn.send(data.encode())  # send data to the client

        conn.close()  # close the connection
            '''


if __name__ == '__main__':
    p=Server0()
    p.processData()
    p.server_program()
