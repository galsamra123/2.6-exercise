"""
Author - Gal Heichal Samra

Program name - client to server connection EX2.6

Description - The prog will make a connection between this client socket to the server
              (both on same computer) and will send commands to the server as long as their
               valid and supported he will get an answer

date   - 28/10/25

"""


import socket
import logging


logging.basicConfig(filename='ex2_6.log ',level=logging.INFO,
                    format='%(asctime)s %(name)s - %(levelname)s - %(message)s')
MAX_PACKET = 1024
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to the server and getting an input
try:
    my_socket.connect(('127.0.0.1', 3034))
    while True:
        request = input('enter your request (use only four chars) \n' )
        while len(request) !=4: #limiting the clients request to 4 bytes only
            print('the request is not valid')
            request = input('enter your request (use only four chars)\n')
            logging.error('the request was not 4 bytes long')
        my_socket.send(request.encode())
        response = my_socket.recv(MAX_PACKET).decode()
        if response == 'Not a command':
            logging.error('the request was not a supported command')
        print(response)
        if request == 'EXIT':
            break
except socket.error as err:
    print('received socket error ')
    logging.critical('received socket error ' + str(err))

