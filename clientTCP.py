import socket 
import time
from datetime import datetime

  
def Main(): 
	# host IP
	host = 'ibiza.dcc.ufla.br'
  
	# Define the port on which you want to connect 
	port = 5008
  
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	# connect to server
	s.connect((host,port))
	# set the timeout in 'micro seconds'
	timeout = 100000
	while True:
		print('digite ping para saber o tempo de resposta do servidor:')
		print('digite loss para saber porcentagem de perda de pacotes:') 
		# message to choose the metric
		message = input()
		# ping metric in 'micro seconds' (time to send and receive a message)
		if message == "ping":
			totalMs = 0
			cont = 0
			for i in range (20):
				msThen = float(datetime.now().strftime("%f"))
				s.send(message.encode('ascii'))
				data = s.recv(1024)
				msNow = float(datetime.now().strftime("%f"))
				time.sleep(0.5)
				difTime = msNow - msThen
				if difTime > 0:
					totalMs = totalMs + (difTime)
					print(difTime, "micro seconds")
					cont+=1
			print("\n media",(totalMs)/cont , "micro seconds")

		# loss metric in '%' (lost packages)
		elif message == "loss":
			errors = 0
			print("\n calculando...")
			for i in range (20):
				msThen = float(datetime.now().strftime("%f"))
				s.send(message.encode('ascii'))
				data = s.recv(1024)
				msNow = float(datetime.now().strftime("%f"))
				if (msNow - msThen) >= timeout or (msNow - msThen) <= 0:
					errors+=1
				time.sleep(0.5)
			print("\n", errors, "% de pacotes perdidos")
  
        # ask the client whether he wants to continue 
		ans = input('\n deseja continuar(s/n) :') 
		if ans == 's': 
			continue
		else: 
			break
    # close the connection 
	s.close() 
  
if __name__ == '__main__': 
	Main() 
