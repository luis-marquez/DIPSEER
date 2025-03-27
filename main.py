import argparse
from classes.experiment_processor import ExperimentProcessor
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process experiment data")
    parser.add_argument("--base_path", required=True, help="Base path of the experiments")
    parser.add_argument("--group", required=False, help="Specify group to process")
    parser.add_argument("--experiment", required=False, help="Specify experiment to process")
    parser.add_argument("--subject", required=False, help="Specify subject to process")

    args = parser.parse_args()

    ExperimentProcessor.process_experiments(args.base_path, args.group, args.experiment, args.subject)
