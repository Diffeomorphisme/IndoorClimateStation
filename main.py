from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

import config


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
			if conn.is_connected():
				print('Connected to MySQL database')
			cursor = conn.cursor()
			cursor.execute(mysql_request)
			return cursor.fetchall()

		except Error as e:
			print(e)

		finally:
			if conn is not None and conn.is_connected():
				conn.close()
				print("Closing connection")


app = Flask("API")


@app.route('/post-data', methods=['POST'])
def main():
	expected_fields = [config.expected_api_call_fields[key] for key in config.expected_api_call_fields.keys()]
	response = {}
	posted_data = {}

	# Check that all fields are present and entered correctly
	# If not, answer with an error and mention which fields are incorrect/missing
	for field in expected_fields:
		if request.args.get(field) is None:
			if "Error" in response.keys():
				response["Error"] += f", '{field}'"
			else:
				response.clear()
				response["Error"] = f"Invalid or missing field, expected: '{field}'"
		else:
			if "Error" not in response.keys():
				response[field] = request.args.get(field)
				posted_data[field] = request.args.get(field)
	if "Error" in response.keys():
		return jsonify(response)

	indoor_climate_database = Database(host=config.database_credentials["host"],
									   name=config.database_credentials["name"],
									   user=config.database_credentials["user"],
									   pwd=config.database_credentials["pwd"])

	posted_key = posted_data[config.expected_api_call_fields["key"]]
	api_keys = indoor_climate_database.fetch_api_keys()

	for key in api_keys:
		if key in posted_key:
			# print(f"API_Key {key} has been authenticated.")
			return jsonify(response)

	response.clear()
	response["Error"] = f"API given {posted_data}"
	return jsonify(response)


if __name__ == '__main__':
	app.run(debug=False, port=8000)
