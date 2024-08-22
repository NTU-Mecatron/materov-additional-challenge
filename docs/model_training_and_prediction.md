## Project Workflow: Model Training & Prediction

This section focuses on training the model and generating predictions.


### 1. Model Training

**Configuration:**

The model training process is controlled by a configuration file named `train_config.yaml`. This file defines settings like:

* `model_path`: Path to the pre-trained model
* `data`: Path to the training data (Make sure to import the file for training !!)
* `epochs`: Number of training epochs
* `imgsz`: Image size for training
* `batch`: Batch size (adjust based on your GPU's memory)
* `workers`: Number of worker processes for data loading
* `patience`: Early stopping patience parameter
* `single_cls`: Flag for single class training
* `close_mosaic`: Flag to close mosaic augmentation
* `cache`: Flag to enable data caching (requires sufficient memory)


**Execution:**

Once you've configured the settings in `train_config.yaml`, start the training process by running:

```
python train.py
```


### 2. Prediction

**Configuration**
The model training process is controlled by a configuration file named `predict_config.yaml`. This file defines settings like:

* `model_path`: Path to the pre-trained model
* `video_path`: Path to the video file on which you want to run object detection using the trained model
* `output_path`: Path where the output video will be saved
* `iou_threshold`: Intersection-over-Union (IoU) threshold for considering a detection as valid
* `csv_path`: Path where the prediction results will be saved in a CSV (Comma-Separated Values) format file
* `display_x-axis`: Width (in pixels) for displaying the output video
* `display_y-axis`: Height (in pixels) for displaying the output video

**Execution:**

Once you've configured the settings in `predict_config.yaml`, start the training process by running:

After training, use the `predict.py` script to make predictions on your data:

```
python predict.py
```

This script will generate a `CSV file` containing the prediction results.

**Conversion of CSV to XLSX:**

Convert CSV to XLSX for better usability, enhanced readability, and added functionality like formatting, data validation, and multi-sheet support.


```
python convert_spreadsheet.py
```
