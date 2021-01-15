import sqlite3

conn = sqlite3.connect("patients")

c = conn.cursor()
"""
c.execute(''' CREATE TABLE checkUp(
            ticket_id       INTEGER     PRIMARY KEY,
            full_name       TEXT(50)    NOT NULL,
            age             INTEGER     NOT NULL,
            address         TEXT(100)   NOT NULL,
            contact         INTEGER,
            time_in         TEXT,
            time_out        TEXT
            )''');
"""
c.execute("INSERT INTO checkUp (full_name, age, address, contact, time_in, time_out) "
          "VALUES ('Sonny Ornido', 21, 'Bagong Nayon', 787724, '1707', '0000')")
c.execute("SELECT * FROM checkUp")
print(c.fetchall())
conn.commit()
conn.close()