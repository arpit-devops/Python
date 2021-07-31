import sqlite3

conn = sqlite3.connect("test.db")

# "SELECT" keyword is use to fetch data form todo table.

command = "select id, list from todo"
result = conn.execute(command)    # this result will give sql object not data, we need to retrive data from this.
#conn.commit()   # commit requird when we need to do some changes / update

# using fetchone() and fetchall()


r =  result.fetchone()   # this will fetch first coloumn form data base.
print(r)


# r = result.fetchall()
# print(r)


