import gzip
import json
import pymysql
import urllib.request
import os

_HOST = '192.168.0.110'
_USER = 'root'
_PASS = '123123'
_API_KEY = '2a2e2792d2a8ba4390599d620397c11e'
_HTML_BASE = '''http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid='''
_GZ_FILE = 'city.list.json.gz'
_CFG_FILE = 'weather.cfg'

class SQL_client:
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password)
		self.cur = self.conn.cursor()
	
	def end(self):
		self.conn.close()

	def drop_db(self):
		sql = '''DROP DATABASE IF EXISTS `weather`'''
		self.cur.execute(sql)
		self.conn.commit()

	def create_db(self):
		sql = '''CREATE DATABASE IF NOT EXISTS `weather`;'''
		self.cur.execute(sql)

		sql = '''USE `weather`;'''
		self.cur.execute(sql)

		sql = '''CREATE TABLE IF NOT EXISTS `cities` (
		`id` INT NOT NULL PRIMARY KEY,
		`title` VARCHAR(150) NOT NULL,
		`country_code` VARCHAR(2) NOT NULL,
		INDEX `title` (`title`),
		INDEX `country_code` (`country_code`)
		);'''
		self.cur.execute(sql)

		self.conn.commit()

	def set(self, data):
		for item in data:
			try:
				sql = '''INSERT INTO `cities` VALUES ('{}', '{}', '{}');'''.format(item['id'], item['name'], item['country'])
				self.cur.execute(sql)
			except Exception:
				sql = ''
		self.conn.commit()

	def get(self, city):
		sql = '''SELECT * FROM `weather`.`cities` WHERE `title`=\'{}\''''.format(city)
		self.cur.execute(sql)
		return self.cur.fetchall()

def first_boot():

	def unpack_data(file):
		with gzip.open(file, 'rb') as f:
			file_content = f.read()
		db = json.loads(file_content)
		return db

	if os.path.isfile(_CFG_FILE):
		with open(_CFG_FILE, 'r', encoding='utf-8') as f:
			config = json.loads(f.read())
	else:
		data = unpack_data(_GZ_FILE)

		db = SQL_client(_HOST, _USER, _PASS)
		db.create_db()
		db.set(data)
		db.end()

		config = dict(host=_HOST, user=_USER, passwd=_PASS, data_file=_GZ_FILE, api_key=_API_KEY, html=_HTML_BASE)

		with open(_CFG_FILE, 'w', encoding='utf-8') as f:
			f.write(json.dumps(config))

	return config



weather_str = '''
Средняя температура: {} (min: {}, max: {})\nДавление: {} мб (гПа)\nВлажность: {} %\nВетер: {} м/с\n
'''
config = first_boot()

db = SQL_client(config['host'], config['user'], config['passwd'])

city_name = ''
while city_name != '0':
	city_name = input('Please, enter city: (0) - exit >')
	for item in db.get(city_name):
		print('\nГород: {}\nКод страны: {}'.format(item[1], item[2]))
		response = urllib.request.urlopen(config['html'].format(item[0]) + config['api_key'])
		cw = json.loads(response.read())
		print(weather_str.format(cw['main']['temp'], cw['main']['temp_min'], cw['main']['temp_max'], 
			cw['main']['pressure'], cw['main']['humidity'], cw['wind']['speed']))
