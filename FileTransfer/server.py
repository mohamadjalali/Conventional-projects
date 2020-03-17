import socket
import sys,os,time

host="127.0.0.1"
port=9001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))

print("Socket Created")
file_name = input("Enter the file_name:")
sock.listen(1)
s,addr = sock.accept()
print(f"Client Connected From: {addr}")

print("Sending File...")

message = file_name.encode("ascii")
s.sendall(message)
time.sleep(0.5)
with open(file_name, "rb") as reader:
    for line in reader:
        s.send(line)
    print("File Send")
print("Socket Closing...")
s.close()
sys.exit()


