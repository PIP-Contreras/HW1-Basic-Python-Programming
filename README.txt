FILE: README.txt

PROJECT TITLE: Iris Dataset Analysis and Visualization

AUTHOR: [Your Name]

DATE: [Date]

DESCRIPTION:
The Python script 'iris_analysis.py' reads the Iris dataset from the 'iris.data' file,
performs calculations on the data, and generates a scatter plot to visualize relationships
between sepal length and sepal width. The script utilizes the Pandas library for data
manipulation and Matplotlib for plotting.

FILES INCLUDED:

- iris_analysis.py: The main Python script that performs data loading, processing, calculations, and plotting.
- iris.data: The Iris dataset file containing sepal length, sepal width, petal length, petal width, and class for each sample.
- iris.names.txt: A file providing information about the Iris dataset, including attribute descriptions and summary statistics.
- requirements.txt: Contains a list of Python packages required to run the script.

SYSTEM REQUIREMENTS:

- Python 3.x (version 3.10 or higher)
- pip (Python package installer)

HOW TO SETUP AND RUN:

1. Ensure Python 3.x (version 3.10 or higher) is installed on your system.

2. Install required Python libraries: Open a terminal or command prompt and run the following command:
   pip install -r requirements.txt
   This will install all necessary packages listed in the 'requirements.txt' file.

3. Running the Script: Navigate to the directory containing 'iris_analysis.py' using the terminal or command prompt. Execute the following command:
   python iris_analysis.py
   Ensure that 'iris.data' and 'iris.names.txt' are in the same directory as the script.

EXPECTED OUTPUT:

The script will print the following to the console:
- The number of rows and columns in the dataset.
- The distinct values in the last column (class).
- Calculations for the 'Iris-setosa' class: number of rows, average sepal length, maximum sepal width, and minimum petal length.

The script will also generate a scatter plot showing the relationship between sepal length and sepal width, with points colored and shaped differently for each Iris species.

TROUBLESHOOTING:

- If the script fails to execute, check that all required packages (Pandas, Matplotlib) are installed correctly and that Python is updated to the latest version (3.10 or higher).

- Verify that the paths to 'iris.data' and 'iris.names.txt' are correct if the script cannot find these files.

- Ensure your 'iris.data' is formatted as expected: comma-separated values with columns for sepal length, sepal width, petal length, petal width, and class.

CONTACT: For any further assistance, please contact [Your Email].