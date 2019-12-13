import sqlite3

con = sqlite3.connect('db/test.db')
cur = con.cursor()
sql = '''create table test(id INTEGER PRIMARY KEY  AUTOINCREMENT,
         txt varchar(30) NOT NULL ,cnt INTEGER);
      '''
try:
    cur.execute(sql)
except sqlite3.Error as e:
    print(e)
except BaseException as e:
    print(e)
finally:
    cur.close() 
    con.close()