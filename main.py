
import sqlite3
import os

#check if file exists
if os.path.exists('db1.db'):
    os.remove('db1.db') # delete file

# connect to db
# if it does not exist -> create + connet
# if it does exist -> connect
conn = sqlite3.connect('db1.db')

# create in memory
# erase after program exit
# conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

# #create table
cursor.execute('''
CREATE TABLE COMPANY(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL default 'unknown',
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
);
''')

#unsafe
# cursor.execute('''
# INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
# VALUES
# (1, 'Paul', 32, 'California', 20000.00),
# (2, 'Allen', 25, 'Texas', 15000.00),
# (3, 'Teddy', 23, 'Norway', 20000.00),
# (4, 'Mark', 25, 'Rich-Mond ', 65000.00),
# (5, 'David', 27, 'Texas', 85000.00),
# (6, 'Kim', 22, 'South-Hall', 45000.00);
# ''')

# safe - one by one
# cursor.execute('''
# INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
# VALUES (?,?,?,?,?);
# ''', (1, 'Paul', 32, 'California', 20000.00))
# cursor.execute('''
# INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
# VALUES (?,?,?,?,?);
# ''', (2, 'Allen', 25, 'Texas', 15000.00))

# safe - multiple
data = [
    (1, 'Paul', 32, 'California', 20000.00),
    (2, 'Allen', 25, 'Texas', 15000.00),
    (3, 'Teddy', 23, 'Norway', 20000.00),
    (4, 'Mark', 25, 'Rich-Mond ', 65000.00),
    (5, 'David', 27, 'Texas', 85000.00),
    (6, 'Kim', 22, 'South-Hall', 45000.00),
]

conn.executemany('''
INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (?,?,?,?,?);
''', data)

import datetime
time_now = datetime.datetime.now().strftime('%H:%M:%S')
address_with_time = 'Texas ' + time_now

cursor.execute('''
UPDATE COMPANY SET ADDRESS = ? WHERE ID = ?;
''', (address_with_time, 6))

cursor.execute('''
DELETE FROM COMPANY WHERE ID = ?
''', (5, ))

cursor.execute('''
SELECT * FROM COMPANY;
''')

print('SELECT * FROM COMPANY result=')
result = cursor.fetchall()
for row in result:
    print(row)

conn.commit() # write changes

conn.close() # close for safety