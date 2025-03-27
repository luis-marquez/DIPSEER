import os
from classes.data_processor import DataProcessor

class ExperimentProcessor:
    @staticmethod
    def process_experiments(base_path, group=None, experiment=None, subject=None):
        data = []

        for group in os.listdir(base_path):
            group_path = os.path.join(base_path, group)

            for experiment in os.listdir(group_path):

                experiment_path = os.path.join(group_path, experiment)

                if os.path.isdir(experiment_path):

                    for subject in os.listdir(experiment_path):
                        subject_path = os.path.join(experiment_path, subject)

                        if os.path.isdir(subject_path):
                            for element in ["images", "labels", "watch_sensor"]:
                                subject_element_path = os.path.join(subject_path, element)
                                if "__" in subject_element_path:
                                    continue
                                data.extend(DataProcessor.process_subject(subject_element_path))
                                filename = f"{group}_{experiment}_{subject}.csv"

                                DataProcessor.save_data_df(data, filename)
        return data

