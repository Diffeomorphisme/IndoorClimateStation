import mysql.connector
from mysql.connector import Error


class Database():
	def __init__(self, host, name, user, pwd):
		self._host = host
		self._name = name
		self._user = user
		self._pwd = pwd

	@property
	def host(self):
		return self._host

	@property
	def name(self):
		return self._name

	@property
	def user(self):
		return self._user

	@property
	def pwd(self):
		return self._pwd

	def fetch_api_keys(self):
		print("Fetching data from Database")
		data = self._request_data("SELECT apiAPIKEY FROM tblAPIKey")
		curated_data = [item[0] for item in data]
		return curated_data

	def _request_data(self, mysql_request: str):
		if type(mysql_request) is not str:
			raise TypeError
		conn = None
		try:
			conn = mysql.connector.connect(host=self._host,
										   database=self._name,
										   user=self._user,
										   password=self._pwd)
			cursor = conn.cursor()
			cursor.execute(mysql_request)
			return cursor.fetchall()

		except Error as e:
			print(e)

		finally:
			if conn is not None and conn.is_connected():
				conn.close()

	def insert_sensor_data(self, api_key, datetime, temperature, humidity):
		print("Inserting data into Database")
		self._insert_data(f"INSERT INTO logtblClimateData (cliSensorID, cliTime, cliTemperature, cliHumidity) VALUES ((" \
						f"SELECT apiSensorID FROM tblAPIKey WHERE apiAPIKey = '{api_key}'), " \
						f"'{datetime}', {temperature}, {humidity}) ")

	def _insert_data(self, mysql_request):
		if type(mysql_request) is not str:
			raise TypeError
		conn = None
		try:
			conn = mysql.connector.connect(host=self._host,
										   database=self._name,
										   user=self._user,
										   password=self._pwd)
			cursor = conn.cursor()
			cursor.execute(mysql_request)
			conn.commit()
			print(f"Added lines: {cursor.rowcount}")

		except Error as e:
			print(e)

		finally:
			if conn is not None and conn.is_connected():
				conn.close()