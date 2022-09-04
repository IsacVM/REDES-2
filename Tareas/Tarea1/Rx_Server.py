import socket

class mySocket_Server:
   
    #Metodo constructor
    def __init__(self,ip="127.0.0.1",port=4500):

    #Creamos objeto del tipo socket
        self.ip=ip
        self.port=port
        self.sockete_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#IPV4 y TCP
        self.sockete_s.bind((ip,port))#Asociamos la Ip de un servidor con un puerto
        self.sockete_s.listen(1)#ponemos a escuchar al servidor y que solo pueda atender 1 petición

    def activa_server(self):
        try:
            while True:
                clientsocket, address=self.sockete_s.accept()#esta linea establece que si 
                #se acepta la conexion del cliente en el servidor en 'address' va a guardar
                #la direccion y el puerto del cliente y se crea el SOCKET y la conexión

                print("Conexion exitosa con cliente:", address)

                #Leer Mensaje
                msg_r=clientsocket.recv(4096).decode() #recibo respuesta del servidor
                print(msg_r)

                #Escribir respuesta
                respuesta=input("\nEscribe tu respuesta: ")
                clientsocket.send(respuesta.encode()) #envio respuesta al cliente en forma de chat

                clientsocket.close()#cerramos conexion con el cliente

        except KeyboardInterrupt:
            self.sockete_s.close()  


if __name__ == "__main__":
    print("\nCHAT DE SERVER ")
    respuesta_s=mySocket_Server("127.0.0.1",4500)
    respuesta_s.activa_server()