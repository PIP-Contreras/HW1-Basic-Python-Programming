FILE: README.txt

PROJECT TITLE: HW1: Basic Python Programming

AUTHOR: DeMarcus Contreras

DATE: 1/24/2025

DESCRIPTION:
The Python script 'iris_analysis.py' reads the dataset from the 'iris.data' file,
makes calculations from the data, and generates a scatter plot to visualize sepal length and sepal width. The script utilizes the Pandas library and Matplotlib.

FILES INCLUDED:

- iris_analysis.py: The main Python script that performs data loading, processing, calculations, and plotting.
- iris.data: The Iris dataset file containing sepal length, sepal width, petal length, petal width, and class for each sample.
- iris.names.txt: A file providing information about the Iris dataset, including attribute descriptions.
- requirements.txt: Contains a list of Python libraries required to run the script.

SYSTEM REQUIREMENTS:

- Python 3.10 or higher
- pip

HOW TO SETUP AND RUN:

1. Make sure that Python 3.10 or higher is installed on your system just in case of any performance issues with the used libraries.

2. Install required Python libraries: Open the terminal and enter 'pip install -r requirements.txt"

3. Running the Script: If you are in VS Code, use the run feature on the top of the window, otherwise, execute the following command:
   python iris_analysis.py
   First, verify that 'iris.data' and 'iris.names.txt' are in the same directory as the script.

EXPECTED OUTPUT:

The script will print the following to the terminal:
- The number of rows and columns in the dataset.
- The possible values in the last column .
- The following calculations for the entries with the 'Iris-setosa' value : number of rows, average sepal length, maximum sepal width, and minimum petal length.

The script will also generate a scatter plot showing the relationship between sepal length and sepal width, with points colored and shaped differently depending on each Iris species each Iris species.

TROUBLESHOOTING:

- If the script fails to execute, verify that all required packages are installed correctly and that Python is up to date. You can check what libraries are being pulled by using 'pip list' in the terminal

- Ensure that all files are locatable in the same directory.

CONTACT: For any further assistance, please contact dcontreras@nmsu.edu.