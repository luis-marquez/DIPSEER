
# DIPSEER: A Dataset for In-Person Student Emotion and Engagement Recognition in the Wild

This project is designed to process experimental data including images, labels, and sensor data. It creates a chronologically ordered dataframe assigning an emotion and attention label to each of the collected data or metadata. The project's structure uses a modular approach with specific classes for each task. The main script allows specifying the `experiment`, `subject`, and `group` from the command line.


## Project Structure
```
project/
├── src/
│   ├── main.py
│   └── classes/
│      ├── image_processor.py
│      ├── label_reader.py
│      ├── sensor_reader.py
│      ├── data_processor.py
│      └── experiment_processor.py
└── README.md
```

## File Descriptions

- **main.py**: Entry point of the script. Processes command-line arguments and calls the necessary methods to process experiments.
- **image_processor.py**: Contains the `ImageProcessor` class with static methods to handle image paths and their metadata.
- **label_reader.py**: Contains the `LabelReader` class with static methods to read labels from JSON files.
- **sensor_reader.py**: Contains the `SensorReader` class with static methods to read sensor data from JSON files.
- **data_processor.py**: Contains the `DataProcessor` class that coordinates the processing of image and sensor data and saves them to CSV files.
- **experiment_processor.py**: Contains the `ExperimentProcessor` class that handles the overall processing of experiments and allows specifying the `group`, `experiment`, and `subject` parameters from the command line.


### Execution
To run the script, use the following command:
python src/main.py --base_path /path/to/experiments --group group_name --experiment experiment_name --subject subject_name

You can omit the `--group`, `--experiment`, and `--subject` arguments if you want to process all groups, experiments, and subjects in the specified base directory.


### Installation

Make sure Python is installed on your system. Clone this repository and navigate to the project directory:

```
git clone git@bitbucket.org:rovitlib/dipseer.git
cd dipseer
```


### Dependencies

This project uses the following Python libraries:

-   `pandas`
-   `argparse`
-   `os`
-   `json`
-   `datetime`

To install `pandas` version 2.2.2, you can use pip:
`pip install pandas`


## Data Access:
`https://www.scidb.cn/en/detail?dataSetId=7856c716c0cc4589a23ee4a23d8a0893`

### Cite this Work
**DIPSER: A Dataset for In-Person Student Engagement Recognition in the Wild**  
Luis Marquez-Carpintero, Sergio Suescun-Ferrandiz, Carolina Lorenzo Álvarez, Jorge Fernandez-Herrero, Diego Viejo, Rosabel Roig-Vila, Miguel Cazorla  
_Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)_  
arXiv: [2502.20209v2](https://doi.org/10.48550/arXiv.2502.20209) [cs.CV], 2 Mar 2025 
