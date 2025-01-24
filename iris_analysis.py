import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Read in the Iris dataset
# The rubric specifies using Pandas functions.
try:
    iris = pd.read_csv('iris.data', header=None)
except FileNotFoundError:
    print("Error: iris.data not found. Please place it in the same directory as the script.")
    exit()

# Adding column names based on iris.names.txt for better readability
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Task 2: Calculate and print the number of rows and columns
# Using Pandas attributes for efficiency as per the rubric
num_rows = iris.shape[0]
num_cols = iris.shape[1]
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

# Task 3: Get all values of the last column and print distinct values
# Using Pandas for efficiency
last_column = iris.iloc[:, -1]
distinct_values = last_column.unique()
print(f"Distinct values in the last column: {', '.join(distinct_values)}")

# Task 4: Calculations for "Iris-setosa"
# Filtering with Pandas for efficiency
iris_setosa = iris[iris['class'] == 'Iris-setosa']

# Calculations
num_rows_setosa = iris_setosa.shape[0]
avg_sepal_length = iris_setosa['sepal_length'].mean()
max_sepal_width = iris_setosa['sepal_width'].max()
min_petal_length = iris_setosa['petal_length'].min()

print(f"Calculations for Iris-setosa:")
print(f"  Number of rows: {num_rows_setosa}")
print(f"  Average sepal length: {avg_sepal_length}")
print(f"  Maximum sepal width: {max_sepal_width}")
print(f"  Minimum petal length: {min_petal_length}")

# Task 5: Scatter plot
# Using Pandas and Matplotlib for plotting
# Creating color and marker maps for better visualization
colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}
markers = {'Iris-setosa': 'o', 'Iris-versicolor': 's', 'Iris-virginica': 'D'}

fig, ax = plt.subplots()
for name, group in iris.groupby('class'):
    ax.scatter(group['sepal_length'], group['sepal_width'],
               color=colors[name], marker=markers[name], label=name)

ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
ax.set_title('Scatter Plot of Sepal Length vs. Sepal Width')
ax.legend()
plt.show()
