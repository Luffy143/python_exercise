# 作者: XWX
# 2022年06月17日10时54分36秒
import socket
import sys
# udp协议传输
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 目标地址构成的元组，包括目标ip与目标端口号
# dest_addr=('192.168.0.166',2000)
dest_addr=(sys.argv[1],2000)    # 给文件传参数

# 编码，以字节流形式发送
client.sendto('hello'.encode('utf8'),dest_addr)
# 以元组的形式接收server端返回的数据
recv_data=client.recvfrom(50)
print(recv_data[0].decode('utf8'))
client.close()

