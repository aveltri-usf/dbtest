import csv
import sqlite3

#import csv and extract data
with open('student_info.csv', 'r') as fin:
  dr = csv.DictReader(fin)
  student_info = [(i['ID'],i['NAME'],i['AGE']) for i in dr]
  print(student_info)

#connect to SQLite
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

#delete exisitng student table
cursor.execute('drop table if exists student')

#create student table
cursor.execute('create table if not exists student(id int primary key, name varchar2(10), age int);')

#insert data into table
cursor.executemany("insert into student (id, name, age) values (?,?,?);", student_info)

#retrieve all data from table
cursor.execute('select * from student;')
results = cursor.fetchall()
print()
for entry in results:
  print(entry)

#update student table
cursor.execute('UPDATE student SET age = 18 WHERE id = 3;')
conn.commit()

#retrieve all data matching given condition from table
cursor.execute('select * from student where name not like "alice";')
results = cursor.fetchall()
print()
for entry in results:
  print(entry)

#close the connection
conn.close()