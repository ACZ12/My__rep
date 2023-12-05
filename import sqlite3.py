import sqlite3
conn=sqlite3.connect("C:\\Users\\adamc\\Documents\\GitHub\\My__rep\\dat.db")
cur=conn.cursor()
names_list=[('Adam', 'Czene'), ('Laszlo', 'Czupper'), ('Levente', 'Karcag'), ('Mate', 'Csernok')]
cur.executemany("""INSERT INTO people)
cur.execute("""CREATE TABLE IF NOT EXISTS people (first_name TEXT, last_name TEXT)""")
conn.commit()



cur.close()
conn.close()