import socket 
import time

  
def Main(): 
	# host IP
	host = '127.0.0.1'
  
	# Define the port on which you want to connect 
	port = 12345
  
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	# connect to server
	s.connect((host,port))
	# set the timeout in 'ms'
	timeout = 1
	
	while True:
		print('digite ping para saber o tempo de resposta do servidor:')
		print('digite loss para saber porcentagem de perda de pacotes:') 
		# message to choose the metric
		message = input()
		# ping metric in 'ms' (time to send and receive a message)
		if message == "ping":
			msThen = float(round(time.time() * 1000))
			for i in range (100):
				s.send(message.encode('ascii'))
				data = s.recv(1024)
				msNow = float(round(time.time() * 1000))
			print((msNow - msThen)/100 , " ms")

		# loss metric in '%' (lost packages)
		elif message == "loss":
			errors = 0
			for i in range (100):
				msThen = float(round(time.time() * 1000))
				s.send(message.encode('ascii'))
				data = s.recv(1024)
				msNow = float(round(time.time() * 1000))
				if (msNow - msThen) >= timeout:
					errors+=1
			print(errors, "% de pacotes perdidos")
  
        # ask the client whether he wants to continue 
		ans = input('\ndeseja cntinuar(s/n) :') 
		if ans == 's': 
			continue
		else: 
			break
    # close the connection 
	s.close() 
  
if __name__ == '__main__': 
	Main() 
