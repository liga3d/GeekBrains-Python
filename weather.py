import gzip
import json
import pymysql

def unpuck_data(file):
	with gzip.open(file, 'rb') as f:
		file_content = f.read()
	db = json.loads(file_content)
	return db

def sql_create_db(host, user, password):
	conn = pymysql.connect(host=host, user=user, password=password)
	cur = conn.cursor()

	sql = '''CREATE DATABASE IF NOT EXISTS `weather`;'''
	cur.execute(sql)

	sql = '''USE `weather`;'''
	cur.execute(sql)

	sql = '''CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT NOT NULL PRIMARY KEY,
	`title` VARCHAR(150) NOT NULL,
	INDEX `title` (`title`)
	);'''
	cur.execute(sql)

	conn.commit()
	conn.close()

def sql_add_data(host, user, password, data):
	conn = pymysql.connect(host=host, user=user, password=password)
	cur = conn.cursor()

	sql = '''USE `weather`;'''
	cur.execute(sql)
	conn.commit()

	for item in data:
		try:
			sql = '''INSERT INTO `cities` VALUES ('{}', '{}');'''.format(item['id'], item['name'])
			cur.execute(sql)
			conn.commit()
		except Exception:
			pass
	conn.close()

def sql_ret_items(host, user, password, city):
	conn = pymysql.connect(host=host, user=user, password=password)
	cur = conn.cursor()

	sql = '''SELECT * FROM weather.cities WHERE title=\'{}\''''.format(city)
	cur.execute(sql)

	return cur.fetchall()

_HOST = '192.168.0.110'
_USER = 'root'
_PASS = '123123'

data = unpuck_data('city.list.json.gz')

sql_create_db(_HOST, _USER, _PASS)
sql_add_data(_HOST, _USER, _PASS, data)

s = ''
while s != '0':
	s = input('Enter city: (0 - exit): >>>')
	for row in sql_ret_items(_HOST, _USER, _PASS, s):
		print(row)

