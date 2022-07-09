import socket

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

local_addr = ('', 2000)
udp_server.bind(local_addr)


recv_data = udp_server.recvfrom(1024)

print(recv_data[0].decode('utf8'))

print(recv_data[1])
# 注释
udp_server.sendto('已收到'.encode('utf8'), recv_data[1])
udp_server.close()
