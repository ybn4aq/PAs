import socket
import datetime

# SOURCES USED: https://docs.python.org/3/library/socket.html , https://www.geeksforgeeks.org/python-simple-port-scanner-with-sockets/
# Getting user's preference of scanning type: Domain or IP address
domain = True
option = input(
    "Welcome to the port scanner! Type 1 to scan an IP Address. Type 2 to scan a hostname."
)
if option == "1":
    domain = False
elif option == "2":
    pass
else:
    print("Eror! Invalid input. Please type either 1 or 0. Exiting program.")
    exit(1)
if domain:
    target = input("Type the domain name. ")
    try:
        # if domain, use socket library's gethostbyname function
        target_sock = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error! Invalid domain name or IP address. Exiting program.")
        exit(1)
else:
    # if ip address, just pass the ip address as a string. socket library knows how to handle it
    target = input("Type an IP address to scan their ports. ")
    target_sock = target
start_port = int(input("What's your start port?"))
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
# Makes a connection timeout
socket.setdefaulttimeout(1)
for i in range(start_port, end_port):
    # attempts to estbalish connection with the port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # will return 0 if port is open
        if sock.connect_ex((target_sock, i)) == 0:
            print("Port " + str(i) + " is open.")
        else:
            print("Port " + str(i) + " is closed.")
        sock.close()
    except socket.error:
        print("Error occured on port " + str(i))
print("Port scanning complete.")
