import os
import json


class LabelReader:
    @staticmethod
    def read_labels(subject_path):
        subject_path = os.path.dirname(subject_path)
        label_path = os.path.join(subject_path, "labels")
        labels = {}
        if os.path.isdir(label_path):
            for label_file in os.listdir(label_path):
                if label_file.endswith(".json"):
                    with open(os.path.join(label_path, label_file), 'r') as file:
                        labels[label_file] = json.load(file)
        return labels