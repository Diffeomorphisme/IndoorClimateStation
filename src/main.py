from fastapi import FastAPI
from pydantic import BaseModel
import datetime

import database.database as database
import src.config as config


class Sensor(BaseModel):
	apiKey: str
	temperature: float
	humidity: float
	datetime: str


app = FastAPI()


@app.get("/time")
def read_time():
	return {"Time": f"{datetime.datetime.now()}"}


@app.post("/post-data")
def add_sensor_data(sensor: Sensor):
	response = {}
	indoor_climate_database = database.Database(host=config.database_credentials["host"],
												name=config.database_credentials["name"],
												user=config.database_credentials["user"],
												pwd=config.database_credentials["pwd"])
	api_keys = indoor_climate_database.fetch_api_keys()

	if sensor.apiKey in api_keys:
		database_insert_success = indoor_climate_database.insert_sensor_data(api_key=sensor.apiKey,
													   datetime=sensor.datetime,
													   temperature=sensor.temperature,
													   humidity=sensor.humidity)
		if database_insert_success:
			response["Status"] = "OK"
			return response

		response.clear()
		response["Error"] = f"Error while inserting data in the database."
		return response

	response.clear()
	response["Error"] = f"API given invalid API key: {sensor.apiKey} "
	return response


if __name__ == "__main__":
	# Use this for debugging purposes only
	import uvicorn

	uvicorn.run(app, host="0.0.0.0", port=5000, log_level="debug")
