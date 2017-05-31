#!/usr/local/bin/python
#-*-coding:utf-8-*-

import MySQLdb

class database(object):
    def __init__(self):
        self.connect()
    # 连接
    def connect(self):
        self.conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="futures", charset="utf8")
        self.cursor = self.conn.cursor()

    # 写入
    def write(self,tablename,date,open,close,high,low,vol):
        self.create(tablename)
        sql = "insert into "+tablename+"(date,open,close,high,low,vol) SELECT %s,%s,%s,%s,%s,%s FROM DUAL WHERE NOT EXISTS(SELECT date FROM  "+tablename+" WHERE date=%s)"
        params = (str(date),float(open),float(close),float(high),float(low),vol,str(date))
        n = self.cursor.execute(sql,params)
        print '%s写入%s，结果%d'%(tablename,str(date),n)

    # 查询
    def select(self,colume="*",db_name='c_table'):
        n = self.cursor.execute("select "+colume+" from "+db_name)
        return self.cursor.fetchall()

    # 建表
    def create(self,tablename):
        if self.cursor.execute("show tables like '%s';"%tablename):
            print tablename +'表已经存在'
            return 0
        else:
            sql =  "CREATE TABLE `%s` ("\
            "`date` varchar(40) NOT NULL,"\
            "`open` decimal(10,0) NOT NULL,"\
            "`close` decimal(10,0) NOT NULL COMMENT '收盘价',"\
            "`low` decimal(10,0) NOT NULL,"\
            "`high` decimal(10,0) NOT NULL,"\
            "`vol` decimal(20,0) NOT NULL COMMENT '成交量\n',"\
            "UNIQUE KEY `date_UNIQUE` (`date`)"\
            ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"%tablename
            if self.cursor.execute(sql)==0:
                print tablename +"表创建成功"

    def close(self):
        self.conn.close()
        # # 更新
        # sql = "update user set name=%s where id=3"
        # param = ("bbb")
        # n = cursor.execute(sql, param)
        # print n
        #
#
# # 删除
# sql = "delete from user where name=%s"
# param = ("aaa")
# n = cursor.execute(sql, param)
# print n
#
    # 关闭

if __name__ == '__main__':
    db = database()
    db.create('ri_table')