import socket

target_ip = input("Enter IP: ")
target_port = int(input("Enter Port: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
if s.connect_ex((target_ip, target_port)) == 0:
    print("Port is OPEN")
else:
    print("Port is CLOSED")
s.close()
