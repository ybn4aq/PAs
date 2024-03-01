import socket
import datetime

domain = True
option = input(
    "Welcome to the port scanner! Type 1 to scan an IP Address. Type 2 to scan a hostname."
)
if option == "1":
    domain = False
elif option == "0":
    pass
else:
    print("Eror! Invalid input. Please type either 1 or 0. Exiting program.")
    exit(1)
if domain:
    target = input("Type the domain name. ")
    try:
        target_sock = socket.gethostbyname(target)  # TODO: error handling
    except socket.gaierror:
        print("Error! Invalid domain name or IP address. Exiting program.")
        exit(1)
else:
    target = input("Type an IP address to scan their ports. ")
    target_sock = target
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
    try:
        if sock.connect_ex((target_sock, i)) == 0:
            print("Port " + str(i) + " is open.")
        else:
            print("Port " + str(i) + " is closed.")
        sock.close()
    except socket.error:
        print("Error occured on port " + str(i))
print("Port scanning complete.")
