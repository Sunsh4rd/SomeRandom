import sqlite3

conn = sqlite3.connect('Whatever.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS WhateverT (
	ID integer PRIMARY KEY NOT NULL,
	Val1 text NOT NULL,
	Val2 integer NOT NULL,
	Val3 text NOT NULL
)''')

conn.commit()  # всегда оставлять в конце эти 2 говны
conn.close()


def insert_some_val(*args):
    a = []
    a.append(tuple(args))

    conn = sqlite3.connect('Whatever.db')
    c = conn.cursor()

    c.executemany('''INSERT INTO WhateverT (Val1, Val2, Val3)
				 	 VALUES (?,?,?)''', a)

    conn.commit()
    conn.close()


def get_from_t():
    conn = sqlite3.connect('Whatever.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM WhateverT''')
    a = (c.fetchall())

    conn.commit()
    conn.close()
    return a
