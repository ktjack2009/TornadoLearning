# 自定义数据库连接
import pymysql
from config import db_options


class Mysql(object):
    def __init__(self):
        options = db_options['default']
        self.host = options['host']
        self.port = options['port']
        self.user = options['user']
        self.pwd = options['password']
        self.dbName = options['dbName']

        self.db = pymysql.connect(host=self.host, user=self.user, password=self.pwd, port=self.port,
                                  database=self.dbName)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def fetch(self, sql, method='one'):
        res = None
        try:
            self.cursor.execute(sql)
            if method == 'one':
                res = self.cursor.fetchone()
            else:
                res = self.cursor.fetchall()
        except Exception as e:
            print(f'查询失败, error={e}')
        return res


if __name__ == '__main__':
    connect = Mysql()
    result = connect.fetch('select * from students where id=1')
    connect.close()
    print(result)
