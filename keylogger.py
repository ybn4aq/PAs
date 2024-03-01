import socket
import datetime

domain = True
option = input(
    "Welcome to the port scanner! Type 1 to scan an IP Address. Type 2 to scan a hostname."
)
if option == "1":
    domain = False
if domain:
    target = input("Type the domain name. ")
    target_sock = socket.gethostbyname(target)  # TODO: error handling
else:
    target = input("Type an IP address to scan their ports. ")
    target_sock = socket.gethostbyaddr(target)  # TODO: error handling
print(target_sock)
start_port = int(input("What's your start port?"))  # TODO: handle improper input
end_port = int(input("What's your end port?"))
time = datetime.datetime.now()
print(
    "Scanning "
    + target
    + " ports "
    + str(start_port)
    + " to "
    + str(end_port)
    + " at "
    + str(time)
)
socket.setdefaulttimeout(1)
for i in range(start_port, end_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex((target_sock, i)) == 0:
        print("Port " + str(i) + " is open.")
    else:
        print("Port " + str(i) + " is closed.")
    sock.close()
print("Port scanning complete.")
