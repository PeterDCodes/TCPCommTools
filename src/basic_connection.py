from socket import socket, AF_INET, SOCK_STREAM


target_ip = '192.168.1.1' #server IP of target device to connect to
target_port = 23 #target port to connect to on device

client_socket = socket(AF_INET, SOCK_STREAM)

try:
    client_socket.connect((target_ip, target_port)) #connect method expects a single arg value as a tuple
    print("Connection success")
except Exception as e:
    print(f"Socket Connect Error {e}")


while(True):
    print(f"Listening for data on {target_ip}:{target_port}")
    #recieve a message
    try:
        data = client_socket.recv(1024) #set buffer size
        print(f"RECEIVED: {data}")
    except Exception as e:
        print(f"Error: {e}")

 

