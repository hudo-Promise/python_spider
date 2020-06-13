import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")
c = conn.cursor()
sql = '''
    create  table company
    (id int primary key not null,
    name  text not null,
    age text not null,
    address char(50),
    salary real
    );

'''
c.execute(sql)
conn.commit()
conn.close()
