import os
import mysql.connector

from dotenv import load_dotenv

load_dotenv()
password=os.getenv('MYSQL_PASSWORD')

# conn = mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password=password
# )
#
# cursor = conn.cursor()
#
# cursor.execute('CREATE DATABASE test_mysql_database')
#
# cursor.close()
# conn.close()

conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password=password,
    database='test_mysql_database',
)
cursor = conn.cursor()
# cursor.execute('CREATE TABLE persons('
#                'id int NOT NULL AUTO_INCREMENT,'
#                'name varchar(14) NOT NULL,'
#                'PRIMARY KEY(id))')

cursor.execute('INSERT INTO persons(name) values("MIKE")')
conn.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

cursor.execute('UPDATE persons set name="Nancy" WHERE name="MIKE"')
cursor.execute('DELETE FROM persons WHERE name = "MIKE"')

cursor.close()
conn.close()
