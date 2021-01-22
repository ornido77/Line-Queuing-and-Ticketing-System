import sqlite3


conn = sqlite3.connect("test")

c = conn.cursor()
"""
c.execute(''' CREATE TABLE date(
            id       INTEGER     PRIMARY KEY,
            username NOT NULL,
            time_in  DATETIME   DEFAULT     CURRENT_TIMESTAMP
            )''')
"""
c.execute("INSERT INTO date(username) VALUES('awaw')")
c.execute("SELECT * FROM date")
print(c.fetchall())
conn.commit()
conn.close()