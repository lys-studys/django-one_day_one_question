#!/usr/bin/env python
# coding=utf-8
import pymysql


DB_HOST = 'xue.kaikeba.com'
DB_PORT = 3306
DB_NAME = 'suanke'
DB_USER = 'lys'
DB_PASSWORD = 'wLQ2uFbMiZEeh7qS'


class Conn:
    def __init__(self):
        self.conn = pymysql.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)

