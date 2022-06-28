#CONNECTION__
import socket
from file_handle_C import File_man

#CONNECTION CLASSES
class connections():
    def __init__(self, **kwargs):
        self.val = ""
        self.FM = File_man()
        
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print(e)
        self.host = '127.0.0.1'
        self.port = 8085
        self.encap = "@"

        
        
        try:
            self.sock.connect((self.host, self.port))
            print("\n[CONNECTED]\n")
        except Exception as e:
            print(e)
       
        

            
    def get_msg(self, **kwargs):
        #WRITE ALL DATA TO FILE
        while True:
            received = ""
            try:
                received = self.sock.recv(1024 * 3).decode()
                print("[RECV]: ", received, "\n")
                print("LENB_OF_MSG::", len(received))
                self.FM.write_file("SERVER.txt", received, "a")

            except Exception as e:
                print("[SOCKET CLOSED]")
                print(str(e)) 
                self.sock.close()   
    
    
    def send_msg(self, **kwargs):
        #try using events
        print("PPPP")
#        time.sleep(1)
        #READ ALL DATA FROM FILES>>
        path = "GAME.txt"
        try:
            self.init_data = str(self.FM.read_file(path))
            print("INIT_DATA:: ", self.init_data)
        except:
            pass
        try:
            while True:
                #print("oooo")
 #               time.sleep(1)
                data = str(self.FM.read_file(path))
                #print("SENDER DATA:: ", data)
                if self.init_data != data:
                    print(f'[SENDING]:: {data}')
                    self.init_data = data

                    try:
                        self.sock.send(data.encode())

                    except Exception as e:
                        print("FUCKUP::SEND_MSG::", str(e))

        except Exception as e:
            print("SENDING_ERROR::", str(e))






