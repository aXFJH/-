

import socket
from getpass import getpass

ADDR=('127.0.0.1',8888)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
def register():
    while True:
        name = input("请输入用户名")
        psw = getpass("请输入密码")
        psw1 = getpass("请再次输入密码")
        if psw!=psw1:
            print("两次密码输入不一致")
            continue
        if (' ' in name) or (' ' in psw):
            print("不可以使用空格")
            continue
        msg="R %s %s"%(name,psw)
        s.send(msg.encode())
        decode = s.recv(128).decode()
        if decode=='OK':
            print("注册成功")
        else:
            print("注册失败")
        return

def main():

    msg = s.recv(1024)

    # s.close()
    print(msg.decode('utf-8'))
    while True:
        print(""
              "===========欢迎==========="
              "====1.注册====2.登录====3.退出===="
              )
        input1 = input("请输入选项")
        if input1=='1':
            register()
        elif input1=='2':
            s.send(input1.encode())
        elif input1=='3':
            s.send(input1.encode())
        else:
            print("请输入正确选项")


if __name__ == '__main__':
    main()

