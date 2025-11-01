"""
Author - Gal Heichal Samra

Program name - Server to client connection EX2.6

Description - The prog will make a connection between this server to the client
              (both on same computer) and will return answers to client if his commands
              are valid and supported

date   - 28/10/25

"""


import socket
from datetime import datetime
import random
import logging


QUEUE_LEN = 1
MAX_PACKET = 1024
SERVER_NAME = 'gals server'
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(('0.0.0.0', 3034))
my_socket.listen(QUEUE_LEN)
logging.basicConfig(filename='ex2_6.log ',level=logging.INFO,
                    format='%(asctime)s %(name)s - %(levelname)s - %(message)s')


def rand():
    """
    the func returns a random number between 1 and 10
    :return: random number between 1 and 10
    """
    return random.randint(1, 10)


def name():
    """
    the func returns the server's name
    :return:  SERVER_NAME
    """
    return SERVER_NAME


def time():
    """
    the func returns the exact time
    :return: readable_time
    """
    now = datetime.now()
    readable_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return readable_time


def main():
    """
    the func connects the server with the clients socket and returns decoded answers
    according to the clients commands
    :return: readable_time or random number (1-10) or SERVER_NAME or socket.close
    """
    while True:
        client_socket, client_address = my_socket.accept()
        try:
            logging.info('a connection was made with client socket')
            while True:
                try:
                    request = client_socket.recv(MAX_PACKET).decode()
                    if request == 'TIME':
                        logging.info('the request is time ' )
                        client_socket.send(time().encode())
                    elif request == 'RAND':
                        logging.info('the request is rand')
                        client_socket.send(str(rand()).encode())
                    elif request == 'NAME':
                        logging.info('the request is name')
                        client_socket.send(name().encode())
                    elif request == 'EXIT':
                        logging.info('the request is exit')
                        client_socket.close()
                        break
                    else:
                        client_socket.send("Not a command".encode())
                except socket.error as err:
                    print('received socket error on client socket')
                    logging.critical('received socket error on client socket' + str(err))
        except socket.error as err:
            print('received socket error on server socket')
            logging.critical('received socket error on server socket' + str(err))
        finally:
            client_socket.close()
            logging.info('the client socket is closed')

if __name__ == "__main__":
    assert(name() == SERVER_NAME)
    assert(1 <= rand() <= 10)
    logging.info('all asserts passed')
    logging.info('server up and running')
    main()

