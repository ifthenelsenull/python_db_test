#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')
bookname = input("Book Name: ")
scifi = input ("Is this a Scifi book? y/n :")

with con:
    
    cur = con.cursor()    
    cur.execute ("DROP TABLE IF EXISTS Book_classifier;")
    cur.execute("CREATE TABLE Book_classifier(Id INT, bookname TEXT, scifi TEXT, )")
    cur.execute("INSERT INTO Book_classifier VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Book_classifier VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO Book_classifier VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO Book_classifier VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO Book_classifier VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO Book_classifier VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO Book_classifier VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO Book_classifier VALUES(8,'Volkswagen',21600)")
    cur.execute('SELECT * FROM Book_classifier')
    allrows = cur.fetchall()
    cur.execute("DROP TABLE Book_classifier")
print(allrows)
print (scifi)
