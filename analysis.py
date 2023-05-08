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


#i also want to analyse the mean, min and max values of this data

#print("These are the minimum values of the different features")
mean = (iris.mean(0,True,None,True))
print(iris.min(0,True,None,True))
min = (iris.min(0,True,None,True))
#print("These are the maximum values of the different features")
print(iris.max(0,True,None,True))
max = (iris.max(0,True,None,True))

arr = mean.to_numpy()
arr2 = min.to_numpy()
arr3 = max.to_numpy()

np.savetxt("outputmean.txt",arr)
np.savetxt("outputmin.txt",arr2)
np.savetxt("outputmax.txt",arr3)


# the code for making the histogram which saves to png
iris.plot(kind="hist")
plt.savefig('histfreq.png')

'''MAKE THIS CODE WORK TO MAKE HISTOGRAMS FOR THE 3 DIFFERENT VARIABLES'''
#the code which will output the summary data into three separate histograms
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

colors = {'Iris-setosa':'g','Iris-virginica':'b','Iris-versicolor':'r'}
fig, ax = plt.subplots()
for i in range(len(iris_feat['petallength'])):
    plt.scatter(iris_feat['petallength'][i], iris_feat['petalwidth'][i],color=colors[iris_species[i]])
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')
ax.set_title('Petal Length vs Width')
ax.legend()
plt.show()