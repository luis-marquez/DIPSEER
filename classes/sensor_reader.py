import os
import json

class SensorReader:
    @staticmethod
    def read_sensors(subject_path):
        sensors_path = SensorReader._get_sensors_path(subject_path)
        if not os.path.isdir(sensors_path):
            return []

        sensor_values = []
        for sensors_file in SensorReader._get_sensor_files(sensors_path):
            data = SensorReader._read_json_file(os.path.join(sensors_path, sensors_file))
            sensor_values.extend(SensorReader._parse_sensor_data(data))

        return sensor_values

    @staticmethod
    def _get_sensors_path(subject_path):
        return os.path.join(os.path.dirname(subject_path), "watch_sensor")

    @staticmethod
    def _get_sensor_files(sensors_path):
        return [f for f in os.listdir(sensors_path) if f.endswith(".json")]

    @staticmethod
    def _read_json_file(file_path):
        with open(file_path, 'r') as file:
            return json.load(file).get("Datos", {})

    @staticmethod
    def _parse_sensor_data(data):
        sensor_values = []
        for type_sensor, values in data.items():
            for value in values:
                value["type_sensor"] = type_sensor
                sensor_values.append(value)
        return sensor_values
