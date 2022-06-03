import signal
import socket
import sys
host='0.0.0.0'
port=8888
ADDR=(host,port)
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,1)
    s.bind(ADDR)
    s.listen(5)
    # signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("listen from 8888.....")
    while True:
        c,addr = s.accept()
        print("连接地址：%s"%str(addr))
        msg="欢迎访问主机8888"
        c.send(msg.encode('utf-8'))
        # c.close()
if __name__ == '__main__':
    main()


