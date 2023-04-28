# pandas will be used to output the summaries into a single text file
import pandas as pd
# numpy will also be called to access the np attributes and evaluate some maths
import numpy as np
from numpy import random
# and finally, matplotlib will be used to save a histogram and display a scatterplot
import matplotlib.pyplot as plt
'''firstly, the data will be called in and displayed using pandas,
 and then output to a text file'''
# reading in the dataset
iris = pd.read_csv("iris_csv.csv")
iris_feat = iris.iloc[:,:-1] # marking the column line using locater
iris_species = iris.iloc[:,-1] 

#print(iris.shape)
#print(iris.describe())
#np.savetxt(iris.txt, iris.describe)

'''
#i also want to analyse the mean, min and max values of this data
iris.groupby('class').agg(['mean','median','max','min'])
iris.groupby('class').agg([np.mean, np.median, np.max, np.min])
print(iris.groupby)'''
print(iris.min())
print(iris.max())
print(iris.mean()) 

# the code for making the histogram which saves to png
fig, ax = plt.subplots()
ax.hist(iris_feat['sepallength'])
#set labels & titles
ax.set_title('Sepal length of all species')
ax.set_xlabel('Centimetres')
ax.set_ylabel('Frequency')
plt.savefig('histogram.png')


# scatter plot to show the relationship between sepal lenght and sepal width
# first setting the colors dictionary for a nice tidy output
colors = {'Iris-setosa':'g','Iris-virginica':'b','Iris-versicolor':'r'}
# creating a figure and axis
fig, ax = plt.subplots()
# plot the diff data points
for i in range(len(iris_feat['sepallength'])):
    plt.scatter(iris_feat['sepallength'][i], iris_feat['sepalwidth'][i],color=colors[iris_species[i]])
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
ax.set_title('Sepal Length vs Width')
ax.legend()
plt.show()