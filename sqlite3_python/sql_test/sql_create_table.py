import sqlite3

conn = sqlite3.connect("test.db")

command = "create table todo (id int, list text)"
conn.execute(command)
print ("done")