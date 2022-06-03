# while True:
#     print(""
#           "===========欢迎==========="
#           "====登录====注册====退出===="
#           )
#

import socket
ADDR=('127.0.0.1',8888)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ADDR)
    msg = s.recv(1024)
    # s.close()
    print(msg.decode('utf-8'))
if __name__ == '__main__':
    main()

