import pandas as pd
import os
import datetime

from classes.image_processor import ImageProcessor
from classes.label_reader import LabelReader
from classes.sensor_reader import SensorReader

class DataProcessor:
    @staticmethod
    def process_subject(subject_path):
        data = []

        image_paths = ImageProcessor.get_image_paths(subject_path)
        if not image_paths:
            return []

        labels = LabelReader.read_labels(subject_path)
        sensor_values = SensorReader.read_sensors(subject_path)

        subject, experiment = DataProcessor._extract_subject_experiment(subject_path)

        image_data = DataProcessor._process_images(image_paths, labels, subject, experiment)
        sensor_data = DataProcessor._process_sensors(sensor_values, subject, experiment)

        data.extend(image_data)
        data.extend(sensor_data)

        return data

    @staticmethod
    def _extract_subject_experiment(subject_path):
        subject = None
        experiment = None
        for part in subject_path.split("/"):
            if "experiment" in part:
                experiment = part
            elif "subject" in part:
                subject = part
        return subject, experiment

    @staticmethod
    def _process_images(image_paths, labels, subject, experiment):
        data = []
        for image_path in image_paths:
            image_time = DataProcessor._extract_image_time(image_path)
            metadata_path = ImageProcessor.get_metadata_path(image_path)
            new_row = {
                "time": image_time,
                "subject": subject,
                "experiment": experiment,
                "image_path": image_path,
                "metadata": metadata_path,
            }
            new_row.update(DataProcessor._extract_labels_for_image(image_time, labels))
            data.append(new_row)
        return data

    @staticmethod
    def _extract_image_time(image_path):
        return os.path.basename(image_path).replace(".png", "").replace("_", ":")

    @staticmethod
    def _extract_labels_for_image(image_time, labels):
        label_data = {}
        for file_label, tags in labels.items():
            for tag in tags:
                if tag["datetime"] == image_time:
                    base_label = file_label.replace(".json", "")
                    if "emotion" in tag:
                        label_data[f"{base_label} emotion"] = tag["emotion"]
                    if "attention" in tag:
                        label_data[f"{base_label} attention"] = tag["attention"]
                    break
        return label_data

    @staticmethod
    def _process_sensors(sensor_values, subject, experiment):
        data = []
        for sensor_value in sensor_values:
            new_row = {
                "subject": subject,
                "experiment": experiment
            }
            for sensor, value in sensor_value.items():
                if sensor == "type_sensor":
                    continue
                elif sensor.lower() == "time":
                    new_row["time"] = value
                else:
                    type_sensor = sensor_value["type_sensor"]
                    new_row[f"{type_sensor} {sensor.lower()}"] = value
            data.append(new_row)
        return data

    @staticmethod
    def save_data_df(data, filename):
        df = pd.DataFrame(data)
        df['time'] = df['time'].apply(lambda x: datetime.datetime.strptime(x, '%H:%M:%S:%f').time())
        df_sorted = df.sort_values(by=['experiment', 'subject', 'time'])

        for column in df_sorted.columns:
            if "emotion" in column or "attention" in column:
                df_sorted[column] = df_sorted[column].fillna(method='ffill')

        df_sorted.to_csv(filename, index=False)
        print(df_sorted)
