# 作者: XWX
# 2022年06月17日09时18分28秒
import socket

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定本地的相关信息，否则则系统会随机分配，下次启动会改变
# 因此通常服务器端要绑定固定的端口号
local_addr = ('', 2000)  # ip地址和端口号，本地ip一般不用写,为空字符串
udp_server.bind(local_addr)

# 从端口接收对方发送来的数据,1024表示本次接收的最大字节数,
recv_data = udp_server.recvfrom(1024)
# 接收到的数据要解码后才能使用
print(recv_data[0].decode('utf8'))
# 元组下标1表示发送方的地址
print(recv_data[1])
# 回应发送方的请求
udp_server.sendto('已收到'.encode('utf8'), recv_data[1])
udp_server.close()
