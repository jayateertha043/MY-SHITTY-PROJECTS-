import socket
def Port_Scan(host,min_port,max_port):
 for port in range(min_port,max_port):
  sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket.setdefaulttimeout(0.5) 
  result=sock.connect_ex((host, int(port)))
  sock.close()
  if not result :
      print('[*] PORT: ' + str(port) + ' is open')
  else :
      print('[*] PORT: ' + str(port) + ' is not open') 
	  

host=input("Enter host : ")
min_port=int(input("Enter min Port range : "))
max_port=int(input("Enter max Port range : "))

Port_Scan(host,min_port,max_port)