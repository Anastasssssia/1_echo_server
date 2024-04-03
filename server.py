import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv()
	if not data:
		break
	msg += data.decode()
	conn.send(data)

print(msg)

conn.close()
