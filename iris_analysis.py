import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Read the Iris dataset using Pandas
iris = pd.read_csv('iris.data', header=None)  # No error handling for simplicity

# Names of columns
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Task 2: Calculate and print the number of rows and columns
num_rows, num_cols = iris.shape 
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

# Task 3: Get all values of the last column and print distinct values
last_column_values = iris.iloc[:, -1].values 
distinct_values = set(last_column_values) 
print(f"Distinct values in the last column: {', '.join(distinct_values)}")

# Task 4: Calculations for "Iris-setosa"
# Using boolean to filter
iris_setosa = iris[iris['class'] == 'Iris-setosa']

# Calculations
num_rows_setosa = len(iris_setosa)
avg_sepal_length = iris_setosa['sepal_length'].mean()
max_sepal_width = iris_setosa['sepal_width'].max()
min_petal_length = iris_setosa['petal_length'].min()
# Printing to terminal
print(f"Calculations for Iris-setosa:")
print(f"  Number of rows: {num_rows_setosa}")
print(f"  Average sepal length: {avg_sepal_length}")
print(f"  Maximum sepal width: {max_sepal_width}")
print(f"  Minimum petal length: {min_petal_length}")

# Task 5: Scatter plot with colors and shapes
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