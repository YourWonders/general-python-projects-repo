from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd, scipy, mglearn

# where i am learning from
# https://files.addictbooks.com/wp-content/uploads/2024/07/Introduction-to-Machine-Learning-with-Python.pdf

iris_dataset = load_iris()

print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))

print(iris_dataset['DESCR'][:193] + '\n...')

print(f"Target names {iris_dataset['data'][:5]}")

print(f"Shape of target: {iris_dataset['target'].shape}")

print(f"Target:\n{iris_dataset['target']}")

# ========================================================================

print('\n')
print('=============\n' * 3)

# ========================================================================
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0
)

print(f"x_train shape {X_train.shape}")
print(f'y_train shape: {y_train.shape}')

print(f'x_test shape: {X_test.shape}')
print(f'y_test shape: {y_test.shape}')


# creating a visual training data graph

iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), marker='o',
                        hist_kwds={'bins':20}, s=60, alpha=.8, cmap=mglearn.cm3)