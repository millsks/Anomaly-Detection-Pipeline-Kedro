# Building and Managing an Isolation Forest Anomaly Detection Pipeline with Kedro

## Overview
Anomaly (fraud) detection pipeline on credit card transaction data using Isolation Forest machine learning model and Kedro framework

Link to article: https://neptune.ai/blog/data-science-pipelines-with-kedro

## Objective
Develop a data science pipeline to detect anomalous (fradulent) credit card transactions with the use of:
- **Isolation Forest** machine learning model - For unsupervised anomaly detection
- **Kedro** - An open-source Python framework for creating reproducible, maintainable, and modular data science code. This framework helps to accelerate data pipelining, enhance data science prototyping, and promote pipeline reproducibility.)

## Motivation
- Explore how unsupervised anomaly detection works, and better understand the concept and implementation of isolation forest
- Leverage Kedro framework to optimally structure data science pipeline projects

## Data
The [credit card transaction data](https://github.com/Fraud-Detection-Handbook/simulated-data-transformed) is obtained from the collaboration between Worldline and Machine Learning Group. It is a realistic simulation of real-world credit card transactions and has been designed to include complicated fraud detection issues.

## General Pipeline Structure
![Alt text](/docs/images/01_DS_Pipeline_Overview.png?raw=true)

## Anomaly Detection Pipeline Structure
![Alt text](/docs/images/05_Anomaly_Detection_Pipeline_Blueprint.png?raw=true)

## Steps
1. Change path to project directory in command line - `cd C:/Anomaly-Detection-Pipeline-Kedro`
2. Initialize Conda virtual environment (create one if not done so) - `conda activate env_kedro`
3. Execute a pipeline run with `kedro run`

Please see the [walkthrough article](https://neptune.ai/blog/data-science-pipelines-with-kedro) for details


# Optional

## Installing and running packaged kedro pipeline
**_NOTE: The `conda env update` command below will be faster if you use `mamba`_**

1. Download the files from the [dist](https://github.com/millsks/Anomaly-Detection-Pipeline-Kedro/tree/main/dist) directory.
2. Create the conda environment using the supplied environment.yml file - `conda env update -n anom-detect-kedro --prune --file environment.yml`
3. Activate the conda environment - `conda activate anom-detect-kedro`
4. Install the packaged kedro pipeline - `pip install anomaly_detection_pipeline_kedro-0.3-py3-none-any.whl --no-deps`
5. Decompress the data files in the pipeline_data files - `cat pipeline_data*|tar zxvf -`
6. Run the pipeline - `python -m anomaly_detection_pipeline_kedro --conf-source=conf-anomaly_detection_pipeline_kedro.tar.gz`
7. In another session run the MLflow server - `mlflow server`
8. Open the MLflow UI in a browser - `http://localhost:5000/`
