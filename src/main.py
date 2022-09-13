from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import datetime


class Sensor(BaseModel):
	apiKeyww: int
	temperature: float
	humidity: float
	time: str


app = FastAPI()


@app.get("/")
def read_root():
	return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}


@app.post("/post-data")
def add_sensor_data(sensor: Sensor):
	print(sensor)
	return {
		"status": "SUCCESS",
		"data": sensor
	}


if __name__ == "__main__":
	# Use this for debugging purposes only
	import uvicorn

	uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
