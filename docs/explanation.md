# Explanation

This tutorial will explain fully about the repo structure, configuration files and how to change parameters if you want to achieve better results.

To quickly get started with the repo and run the inference, refer to the [Getting Started](getting_started.md) tutorial instead.

**Table of Contents**
- [Repository Contents](#repository-contents)
- [Model Training](#model-training)
- [Prediction](#prediction)

## Repository Contents

**[Configuration Folder](config/):**
- `train.yaml`: Configuration file for training parameters used in `train.py`.
- `predict_no_slicer.yaml`: Configuration file for prediction settings used in `predict_no_slicer_on_images.py` & `predict_no_slicer.py`.
- `predict_with_slicer.yaml`: Configuration file for prediction settings used in `predict_with_slicer_on_images.py` & `predict_with_slicer.py`.

**[Spreadsheet Folder](spreadsheet/):**
- `spreadsheet.csv`: CSV file generated from running `predict_with_slicer.py` only. Other prediction scripts do not generate this file.
- `spreadsheet.xlsx`: Automatically convert CSV file to XLSX file.

**[Source Folder](src/):**
- `train.py`: Script for training the YOLO model.
- `predict_no_slicer_on_images.py`: Script for running predictions using the trained model with no slicer on images.
- `predict_no_slicer.py`: Script for running predictions using the trained model with no slicer.
- `predict_with_slicer_on_images.py`: Script for running predictions using the trained model with with slicer on images.
- `predict_with_slicer.py`: Script for running predictions using the trained model with no slicer on images.
- `convert_spreadsheet.py`: Utility script for converting data from spreadsheets into the required format for training and prediction.

**[Training Results Folder](training_results/):**
- `base_model_100_epochs`: Trained on YOLO V10M with 100 epochs. The output will be termed `Base Model` on subsequent lines.
- `fine_model_100_epochs`: Trained from output of `Base Model` with 100 epochs.
- `fine_model_150_epochs`: Trained from output of `Base Model` with 150 epochs.
- `fine_model_200_epochs`: Trained from output of `Base Model` with 150 epochs. This model turned out to be worse than the `fine_model_150_epochs`.
- `yolov10s_no_pretrained`: YOLO V10S from online (no pretrained) with 150 epochs.

## Model Training

**Configuration**

The model training process is controlled by a configuration file named `train.yaml`. This file defines the following settings:

* `model_path`: Path to the model to be trained
* `data`: Path to the training data `.yaml` file (likely an absolute path since the data directory is not inside this package)
* `epochs`: Number of training epochs
* `imgsz`: Image size for training (usually 640)
* `batch`: Batch size (default is 32; increase if you have a large GPU with much more memory)
* `workers`: Number of worker processes for data loading
* `patience`: Early stopping if there is no improvement after this number of epochs 
* `single_cls`: Flag for single class training
* `close_mosaic`: Flag to close mosaic augmentation
* `cache`: Flag to enable data caching (requires sufficient memory but enable faster training)

For a full explanation, refer to the [Ultralytics documentation](https://docs.ultralytics.com/modes/train/#train-settings).

**Execution:**

Once you've configured the settings in `train.yaml`, start the training process by running:

```bash
# Reminder: You need to be at the root of the directory to run this command
python src/train.py
```


## Prediction

**Configuration**

The model training process is controlled by configuration files named `predict_no_slicer.yaml` or  `predict_with_slicer.yaml`. These files define the following settings:

* `model_path`: Path to the model to do inference with.
* `input_path`: Path to the video file on which you want to run object detection using the trained model.
> **Note:** Input path can also be a dicrectory of images. However, in this case you need to use `predict_with_slicer_on_images.py` or `predict_no_slicer_on_images.py`.
* `output_path` (Optional): Path where the output video will be saved. If not given, video will not be saved.
* `iou_threshold`: Intersection-over-Union (IoU) threshold for considering a detection as valid for eliminating overlapping boxes; the lower the value, the more boxes will be dropped.

* `confidence`: The minimum confidence required for each box; the higher the value, the fewer boxes will be detected.
> Warning: You will notice that the preset values for `iou_threshold` and `confidence` are differnt between `predict_no_slicer.yaml` and `predict_with_slicer.yaml`. This is intentional. The values are set to optimal for each method.

> Tips: If there are many false positive, increase the `confidence` (Range 0-1, change in increment of 0.05). If there are many overlapping boxes of the same object, reduce the `iou_threshold`(Range 0-1, change in increment of 0.05).
* `csv_path` (Optional): Path where the prediction results will be saved in a CSV format file, which will then be converted to an XLSX file when exiting the script. Only available in `predict_with_slicer.yaml`. If not given, no CSV file will be saved.
* `display_x-axis` & `display_y-axis` (Optional) : Width (in pixels) & Height (in pixels) for displaying the output video. If not given, the annotated frames will not be displayed.

**Execution**

After training, execute the appropirate `predict` python file based on preference to make predictions on your data:

* `predict_no_slicer_on_images.py:` Script for running predictions using the trained model with no slicer on an image directory.
* `predict_no_slicer.py:` Script for running predictions using the trained model with no slicer.
* `predict_with_slicer_on_images.py:` Script for running predictions using the trained model with with slicer on an image directory.
* `predict_with_slicer.py:` Script for running predictions using the trained model with no slicer on images.

