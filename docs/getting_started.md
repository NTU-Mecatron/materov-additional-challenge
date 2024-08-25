# Installation

This tutorial will help you install the repo and run inference on your desired video. 

For a full explanation of the repo, refer to the [next tutorial](explanation.md).

**Table of Contents**
- [Prerequisites](#prerequisites)
   - [Installing Python](#installing-python)
   - [Installing Git-LFS](#installing-git-lfs)
   - [Installing required libraries](#installing-required-libraries)
   - [Cloning the Project](#cloning-the-project)
- [Run inference](#run-inference)
   - [Inference with slicer](#inference-with-slicer)
   - [Inference without slicer](#inference-without-slicer)

## Pre-requisites

### Installing Python

To install Python, follow these steps:

1. Visit the [Python download page](https://www.python.org/downloads/).
2. Download the latest version suitable for your operating system.
3. Run the installer and ensure that you check the box to "Add Python to PATH" before proceeding.

For detailed instructions, refer to the official [Python installation guide](https://docs.python.org/3/using/index.html).

### Installing Git-LFS

To install Git-LFS:

1. Visit the [Git-LFS installation guide](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage).
2. Follow the installation instructions for your operating system.
3. After installation, run the following command to enable Git-LFS:

   ```bash
   git lfs install
   ```

### Installing required libraries

For pytorch installation, it is recommended that you install it with cuda support. Follow this [guide](https://pytorch.org/get-started/locally/) to install pytorch for your device.

After this, you can install the other required libraries using the following command:

```bash
pip install ultralytics supervision pandas XlsxWriter 
```
> Note:
- For any issues with PyTorch installation, refer to the [PyTorch guide](https://pytorch.org/get-started/locally/).
- For problems with Ultralytics installation, check the [Ultralytics guide](https://docs.ultralytics.com/quickstart/).
- For more details on Pandas, refer to the [Pandas guide](https://pandas.pydata.org/docs/getting_started/install.html).
- For more details on XlsxWriter, refer to the [XlsxWriter guide](https://xlsxwriter.readthedocs.io/getting_started.html).

### Cloning the Project

You can clone the project using the following command in the terminal:

```bash
git clone https://github.com/NTU-Mecatron/materov-additional-challenge.git
```

## Run inference

> Warning: To run any of the python code, you have to be at the root of this directory due to the way that Python relative imports work.

### Inference with slicer 

You need to first modify the `input_path` in the [predict_with_slicer.yaml](../config/predict_with_slicer.yaml) to the appropriate video or image directory path. It can be an absolute or relative path. 

By default, the annotated frames will not be saved. If you want to save the annotated frames into an output video file, uncomment the `output_path` in `predict_with_slicer.yaml` and enter the desired `.mp4` file name. Then run the following command:

```bash
# Recommended for maximum accuracy
# Recommended for this competition
python src/predict_with_slicer.py
```
![](slicer_preview.gif)

### Inference without slicer

Similarly, you also need to modify the `input_path` and `output_path` in [predict_no_slicer.yaml](../config/predict_no_slicer.yaml). Note that for this method, you cannot generate the spreadsheets. Then run the following command:

```bash
# Recommended for real-time inference at slightly lower accuracy
# Please modify the input_path in the predict_no_slicer.yaml file
python src/predict_no_slicer.py
```

![](no_slicer_preview.gif)

For more explanation on modifying parameters, refer to [explanation](explanation.md).