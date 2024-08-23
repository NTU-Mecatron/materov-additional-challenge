# Brittle Star Detection with YOLO

## Overview

This repository contains the resources needed to train YOLO models for detecting brittle stars. Developed by [Mecatron](https://mecatron.sg/), this project is part of the 2024 OER MATE ROV Ocean Exploration Video Challenge.

## Repository Contents

**[Configuration Folder](config/):**
- **`train.yaml`**: Configuration file for training parameters used in `train.py`.
- **`predict_no_slicer.yaml`**: Configuration file for prediction settings used in `predict_no_slicer_on_images.py` & `predict_no_slicer.py`.
- **`predict_with_slicer.yaml`**: Configuration file for prediction settings used in `predict_with_slicer_on_images.py` & `predict_with_slicer.py`.

**[Documentation Folder](docs/):**
- **`installation.md`**: Step-by-step instructions for setting up the environment and dependencies.
- **`model_training_and_prediction.md`**: Detailed guide on training the model and making predictions.

**[Spreadsheet Folder](spreadsheet/):**
- **`spreadsheet.csv`**: CSV file generated from running `predict_with_slicer_on_images.py` & `predict_with_slicer.py` only. **Other predict python files with generate video.
- **`spreadsheet.xlsx`**: Automatically convert CSV file to XLSX file.

**[Source Folder](src/):**
- **`train.py`**: Script for training the YOLO model.
- **`predict_no_slicer_on_images.py`**: Script for running predictions using the trained model with no slicer on images.
- **`predict_no_slicer.py`**: Script for running predictions using the trained model with no slicer.
- **`predict_with_slicer_on_images.py`**: Script for running predictions using the trained model with with slicer on images.
- **`predict_with_slicer.py`**: Script for running predictions using the trained model with no slicer on images.
- **`convert_spreadsheet.py`**: Utility script for converting data from spreadsheets into the required format for training and prediction.

**[Training Results Folder](training_results/):**
- **`base_model_100_epochs`**: Trained on YOLO V10M (Base Model) with 100 epochs.
- **`fine_model_100_epochs`**: Trained from output of Base Model with 100 epochs.
- **`fine_model_150_epochs`**: Trained from output of Base Model with 150 epochs.
- **`yolov10s_no_pretrained`**: YOLO V10S with no pretrained with 150 epochs.

## Tutorials

- **[Setup Guide](docs/installation.md):** Step-by-step instructions for setting up the environment and dependencies.
- **[Model Training & Prediction Guide](docs/model_training_and_prediction.md):** Detailed guide on training the model and making predictions.