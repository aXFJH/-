import pymysql
import hashlib

salt=b"*#06#"

def jiami(passwd):
    md_ = hashlib.md5(salt)
    md_.update(passwd.encode())
    return md_.hexdigest()



class Datebase:
    def __init__(self):
        self.connect = pymysql.connect(host='localhost', port=3306, user='root', password='xuhao', database='dict',
                                  charset='utf8')
        self.cursor = self.connect.cursor()
    def register(self,name,psw):

        sql="select * from user where name='%s'"%name
        self.cursor.execute(sql)
        fetchone = self.cursor.fetchone()
        if fetchone:
            return False
        psw = jiami(psw)
        print(psw)
        try:
            sql="insert into user (name,passwd) values (%s,%s)"
            self.cursor.execute(sql,[name,psw])
            self.connect.commit()
            return  True
        except:
            self.connect.rollback()
            return False
