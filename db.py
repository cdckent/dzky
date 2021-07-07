import pymysql
import yaml
from readyml import ReadConfig
rc=ReadConfig()
class DB:
    def __init__(self):
        self.conn = pymysql.connect(host= rc.read_SQL_config('host'),
                                    port=3306,
                                    user='root',
                                    passwd='Xiaoka520',  # password也可以
                                    db='interfacetest',    # interfacetest 可建表
                                    charset='utf8')  # 如果查询有中文需要指定数据库编码
        self.cur = self.conn.cursor()

    def __del__(self):  # 析构函数，实例删除时触发
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self, name):
        result = self.query("select * from user where name='{}'".format(name))
        return True if result else False

    def del_user(self, name):
        self.exec("del from user where name='{}'".format(name))

if __name__ == '__main__':
    db=DB()
    c=db.query("select age, id from user where name='李四'")
    print(c)
