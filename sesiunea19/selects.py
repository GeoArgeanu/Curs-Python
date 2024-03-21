import sqlite3
from curs_python.sesiunea19 import constants
from pprint import pprint

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()

# -------5
select_all_countries = '''
select * from countries
order by name
'''

cursor.execute(select_all_countries)
pprint(cursor.fetchall())


count_all_countries = '''
select count(*) from countries;
'''
cursor.execute(count_all_countries)
pprint(cursor.fetchone())


# ------6
print(50*'*')

countries_population_20m = '''
select * from countries where population >20;
'''
cursor.execute(countries_population_20m)


# ------7
counties_starting_white_c = '''
select * from countries where name like 'C%';
'''

cursor.execute(counties_starting_white_c)
pprint(cursor.fetchall())

conn.close()