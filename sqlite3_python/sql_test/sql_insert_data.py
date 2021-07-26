import sqlite3

conn = sqlite3.connect("test.db")

command = "insert into todo (id, list) values(1, 'do ldap')"
conn.execute(command)
conn.commit()   # we need to commit as we want it to be done or not.
print ("done")