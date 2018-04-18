# !/usr/bin/env python
# -*- coding:utf-8 -*-
import mysql.connector

class Mysql:

    def __init__(self):
        self._config={
            'host': 'localhost',
            'user': 'root',
            'password': 'test',
            'port': 3306,
            'database': 'NetMusic',
            'charset':'utf8'
        }
        self._conn = self.connectToDatabase()
        if(self._conn):
            print("True")
            self._cursor = self._conn.cursor()

    def connectToDatabase(self):
        conn = False
        try:
            conn = mysql.connector.connect(**(self._config))
            #cursor1 = conn.cursor()
            '''
            #cursor1.execute('create table user (id varchar(20) primary key)')
            sql_str = 'insert into user (id) values (1)'
            print(sql_str)
            cursor1.execute(sql_str)
            conn.commit()
            '''
            print("连接成功！")
        except mysql.connector.Error as e:
            print('connect fails! {}'.format(e))
            conn = False
        #self.conn = mysql.connector.connect(user_string,password_string,database_string)
        return conn


    def insertToDatabase(self,sql_string):
        print(sql_string.encode("utf-8"))
        self._cursor.execute(sql_string.encode("utf-8"))
        s = self._conn.commit()
        #print ("ID of last record is ", int(self._cursor.lastrowid))  # 最后插入行的主键ID
        return self._cursor.lastrowid;
