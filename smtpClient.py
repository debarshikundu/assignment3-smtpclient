from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    mailserver = ("127.0.0.1", 1025)
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)

    recv = clientSocket.recv(1024).decode()
   

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    

    # Send MAIL FROM command and handle server response.
    mailFrom = 'MAIL FROM: <dk3153@nyu.edu>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    

    # Send RCPT TO command and handle server response.
    rcptTo = 'RCPT TO: <dk3153@nyu.edu>\r\n'
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()

    # Send DATA command and handle server response.
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()

    # Send message data.
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()

    # Send QUIT command and handle server response.
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recv6 = clientSocket.recv(1024).decode()


if __name__ == '__main__':
    smtp_client((1025, '127.0.0.1'))