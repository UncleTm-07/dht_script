#!/usr/bin/env python
import argparse
import os
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 15


def get_data():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    except Exception as e:
        return None

    if humidity is not None and temperature is not None:
        return humidity, temperature
    else:
        return None


def write_data(directory, data):
    absolute_path = os.path.join(directory, "dht.txt")

    with open(absolute_path, "w") as f:
        f.write("Temperature - ")
        f.write(data[1])
        f.write("Humidity - ")
        f.write(data[0])
        f.write("Timestamp - ")
        f.write(time.time())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a file in the specified directory.")
    parser.add_argument("directory", help="Path to the directory where the file should be created.")
    args = parser.parse_args()
    directory = args.directory

    data = get_data()

    if data is not None:
        write_data(directory, data)
        print("Data created")
    else:
        print("Data not created")
