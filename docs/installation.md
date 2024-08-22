# Installation

Before installing the packages for this project, ensure that Python and Git-LFS are installed.

## Installing Python

To install Python, follow these steps:

1. Visit the [Python download page](https://www.python.org/downloads/).
2. Download the latest version suitable for your operating system.
3. Run the installer and ensure that you check the box to "Add Python to PATH" before proceeding.

For detailed instructions, refer to the official [Python installation guide](https://docs.python.org/3/using/index.html).

## Installing Git-LFS

To install Git-LFS:

1. Visit the [Git-LFS installation guide](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage).
2. Follow the installation instructions for your operating system.
3. After installation, run the following command to enable Git-LFS:

   ```bash
   git lfs install
   ```

## Cloning the Project

You can clone the project using the following command:

```bash
git clone https://github.com/NTU-Mecatron/materov-additional-challenge.git
```

## Libraries Installation

### Installing All Required Libraries

Once Python is installed, use the following command to install all the required libraries:

- Pytorch
- Ultralytics
- Pandas
- XlsWriter
- Supervision

```bash
pip install torch ultralytics pandas XlsxWriter supervision
```

> Note:
- For any issues with PyTorch installation, refer to the [PyTorch guide](https://pytorch.org/get-started/locally/).
- For problems with Ultralytics installation, check the [Ultralytics guide](https://docs.ultralytics.com/quickstart/).
- For more details on Pandas, refer to the [Pandas guide](https://pandas.pydata.org/docs/getting_started/install.html).
- For more details on XlsxWriter, refer to the [XlsxWriter guide](https://xlsxwriter.readthedocs.io/getting_started.html).