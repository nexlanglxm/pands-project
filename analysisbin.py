'''column_subset = [
    "sepal length",
    "sepal width",
    "petal length",
    "petal width",
    "flower",
]'''

'''
#providing values for the new row to be input as a dictionary
new_row = ("Sepal length",
    "Sepal width",
    "Petal length",
    "Petal width",
    "Flower",
    )
Iris.loc[0] = new_row
'''
# pandas will be used to output the summaries into a single text file
import pandas as pd
# numpy will also be called to access the np attributes and evaluate some maths
import numpy as np
from numpy import random
# and finally, matplotlib will be used to save a histogram and display a scatterplot
import matplotlib.pyplot as plt

iris = pd.read_csv("iris_csv.csv")
iris_feat = iris.iloc[:,:-1] # marking the column line using locater
iris_species = iris.iloc[:,-1] 

mean = (iris.mean(0,True,None,True))

iris.plot(kind="hist")

plt.show()