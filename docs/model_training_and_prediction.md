## Project Workflow: Model Training & Prediction

This section focuses on training the model and generating predictions.


### 1. Model Training

**Configuration:**

The model training process is controlled by a configuration file named `train.yaml`. This file defines settings like:

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

Once you've configured the settings in `train.yaml`, start the training process by running:

```
python train.py
```


### 2. Prediction

**Configuration**
The model training process is controlled by a configuration file named `predict_no_slicer.yaml` or  `predict_with_slicer`. These files defines settings like:

* `model_path`: Path to the pre-trained model
* `input_path`: Path to the video file on which you want to run object detection using the trained model.
> **Note:** Input path can also be a dicrectory of images. However, in this case you need to use `predict_with_slicer_on_images` or `predict_no_slicer_on_images`.
* `output_path (Optional)`: Path where the output video will be saved
* `iou_threshold`: Intersection-over-Union (IoU) threshold for considering a detection as valid for eliminating overlapping boxes, the lower the value, the more boxes should be dropped.

* `confidence`: The minimum confidence required for each box, the higher the value, the fewer boxes will be detected.
* `csv_path (Optional)`: Path where the prediction results will be saved in a CSV (Comma-Separated Values) format file
* `display_x-axis` & `display_y-axis (Optioanl)` : Width (in pixels) & Height (in pixels) for displaying the output video.

> The default settings are optimal as they are. If there are many false positive, increse the `confidence` (Range 0-1, change in increment of 0.05), if there are many overlapping boxes of the same object, reduce the `iou_threshold`(Range 0-1, change in increment of 0.05).

**Execution:**

After training, execute the appropirate `predict` python file based on preference  to make predictions on your data:

* `predict_no_slicer_on_images.py:` Script for running predictions using the trained model with no slicer on images.
* `predict_no_slicer.py:` Script for running predictions using the trained model with no slicer.
* `predict_with_slicer_on_images.py:` Script for running predictions using the trained model with with slicer on images.
* `predict_with_slicer.py:` Script for running predictions using the trained model with no slicer on images.
* `convert_spreadsheet.py:` Utility script for converting data from spreadsheets into the required format for training and prediction.

```
python predict.py
```

> Replace predict.py with the appropriate python file above.

This script will generate a `CSV file` containing the prediction results and automatically convert the CSV file to XLSX file.
