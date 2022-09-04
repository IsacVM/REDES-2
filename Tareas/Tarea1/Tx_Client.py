import socket

class mySocket_Client:
   
    #Método constructor
    def __init__(self,ip="127.0.0.1",port=4500):

     #Creamos objeto del tipo socket
        self.ip=ip 
        self.port=port
        self.sockete_c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#IPV4 y TCP
        self.sockete_c.connect((ip,port))#Asociamos la Ip y puerto de destino al socket
  
    #Función para enviar mensaje
    def f_send(self,mensaje):
        
        self.sockete_c.send(mensaje.encode())
        self.sockete_c.close()

    #Función para recibir mensaje
    def f_get(self):   

        self.msg_r=self.sockete_c.recv(4096).decode() #recibo respuesta del servidor
        # en un buffer de a lo mas 1024 bytes  
        print(self.msg_r)   
       
                   

if __name__ == "__main__":
    print("\nCHAT DE CLIENTE\n ")
    enviador=mySocket_Client("127.0.0.1",4500)
    mensa=input("Escribe tu mensaje: ")
    enviador.f_send(mensa)
    enviador.f_get()
