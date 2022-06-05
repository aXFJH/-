import signal
import socket
import sys
from multiprocessing import Process
from dict_db import Datebase
host='0.0.0.0'
port=8888
ADDR=(host,port)
datebase = Datebase()


def register(c,data):
    split = data.split(' ')
    name=split[1]
    psw=split[2]
    if datebase.register(name,psw):
        c.send(b'OK')
    else:
        c.send(b'Fail')


def request(c):
    while True:
        decode = c.recv(1024).decode()
        print(c.getpeername(),":",decode)
        if decode[0]=='R':
            register(c,decode)


def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(ADDR)
    s.listen(5)
    # signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("listen from 8888.....")
    while True:
        try:
            c,addr = s.accept()
            print("连接地址：%s"%str(addr))
            msg="欢迎访问主机8888"
            c.send(msg.encode('utf-8'))
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务退出")
        # c.close()
        except Exception as e:
            print(e)
            continue
        #创建新的进程处理客户端请求
        client = Process(target=request, args=(c,))
        client.daemon=True
        client.start()


if __name__ == '__main__':
    main()


