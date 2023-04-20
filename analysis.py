#pandas will be used to output the summaries into a single text file
import pandas as pd
#numpy will also be called to access the np attributes and evaluate some maths
import numpy as np
#and finally, matplotlib will be used to save a histogram and display a scatterplot
import matplotlib.pyplot as plt
'''firstly, the data will be called in and displayed using pandas,
 and then output to a text file'''

'''column_subset = [
    "sepal length",
    "sepal width",
    "petal length",
    "petal width",
    "flower",
]'''
Iris = pd.read_csv(
    "iris.data",
    #usecols=column_subset,
    nrows=149
    )

#providing values for the new row to be input as a dictionary
new_row = ("Sepal length",
    "Sepal width",
    "Petal length",
    "Petal width",
    "Flower",
    )
Iris.loc[0] = new_row
'''
Iris.columns = ["Sepal length",
    "Sepal width",
    "Petal length",
    "Petal width",
    "Flower",
    ]'''
print(Iris)
#Iris.head()
#Iris.info()
#Iris.to_frame(iris.txt)
#df.to_frame(iris.txt)











'''i also want to analyse the mean, min and max values of this data'''
#pd.DataFrame(filename)
#print(df)

'''the code for making the histogram which saves to png'''