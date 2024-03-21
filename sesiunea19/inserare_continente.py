import sqlite3
from curs_python.sesiunea19 import constants

# ----2
conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()

continents = "Asia AS,Africa AF,North_America NA,South_America SA,Antarctica AN,Europe EU,Australia AU"

insert_continents = []

for c in continents.split(','):
    # print(c.split())
    name, code = c.split()
    insert_continents.append((name, code))

print(insert_continents)

script = '''
INSERT INTO continents(name, code)
VALUES(?, ?);
'''

cursor.executemany(script, insert_continents)
conn.commit()
conn.close()