#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
  
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='king665206', db='test')
# 创建游标
cursor = conn.cursor()
'''
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
conn.commit()
cursor = conn.cursor()'''
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭游标	
cursor.close()
# 关闭连接
conn.close()