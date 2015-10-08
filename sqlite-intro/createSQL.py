import sqlite3

conn = sqlite3.connect("demo.db")

c = conn.cursor()

q = "create table people(name text, age integer, id integer)"
print c.execute(q)

q = "create table classes(name text, grade integer, id integer)"
print c.execute(q)

conn.commit()
