# pandas will be used to output the summaries into a single text file
import pandas as pd
# numpy will also be called to access the np attributes and evaluate some maths
import numpy as np
from numpy import random
# matplotlib will be used to save a histogram and display a scatterplot
import matplotlib.pyplot as plt
# seaborn for fun after the rest is finished
import seaborn as sns
'''firstly, the data will be called in and displayed using pandas,
 and then output to a text file'''
# reading in the dataset
iris = pd.read_csv("iris.data")
iris_feat = iris.iloc[:,:-1] # marking the column line using locater
iris_species = iris.iloc[:,-1] 

petallength = (iris_feat['petallength']) #calling from the dictionary that was created
sum_petallength = petallength.to_numpy() #creating the ndarray
np.savetxt("sumpetlength.txt", sum_petallength) #calling in the array into the numpy savetxt

petalwidth = (iris_feat['petalwidth']) #calling from the dictionary that was created
sum_petalwidth = petalwidth.to_numpy() #creating the ndarray
np.savetxt("sumpetwidth.txt", sum_petalwidth) #calling in the array into the numpy savetxt

sepallength = (iris_feat['sepallength']) #calling from the dictionary that was created
sum_sepallength = sepallength.to_numpy() #creating the ndarray
np.savetxt("sumseplength.txt", sum_sepallength)

sepalwidth = (iris_feat['sepalwidth']) #calling from the dictionary that was created
sum_sepalwidth = sepalwidth.to_numpy() #creating the ndarray
np.savetxt("sumsepwidth.txt", sum_sepalwidth)

mean = (iris.mean(0,True,None,True))
arr = mean.to_numpy()
np.savetxt("outputmean.txt",arr)

min = (iris.min(0,True,None,True))
arr2 = min.to_numpy()
np.savetxt("outputmin.txt",arr2)

max = (iris.max(0,True,None,True))
arr3 = max.to_numpy()
np.savetxt("outputmax.txt",arr3)

#the code which will output the summary data into separate histograms
fig, ax = plt.subplots()
ax.hist(iris_feat['sepallength'])
#set labels & titles
ax.set_title('Sepal length of all species')
ax.set_xlabel('Centimetres')
ax.set_ylabel('Frequency')
#calling in the savefig function
plt.savefig('histsepallength.png')

fig, ax = plt.subplots()
ax.hist(iris_feat['sepalwidth'])
#set labels & titles
ax.set_title('Sepal width of all species')
ax.set_xlabel('Centimetres')
ax.set_ylabel('Frequency')
plt.savefig('histsepalwidth.png')

fig, ax = plt.subplots()
ax.hist(iris_feat['petallength'])
#set labels & titles
ax.set_title('Petal length of all species')
ax.set_xlabel('Centimetres')
ax.set_ylabel('Frequency')
plt.savefig('histpetallength.png')

fig, ax = plt.subplots()
ax.hist(iris_feat['petalwidth'])
#set labels & titles
ax.set_title('Petal width of all species')
ax.set_xlabel('Centimetres')
ax.set_ylabel('Frequency')
plt.savefig('histpetalwidth.png')

'''for the pairs of variables'''
# scatter plot to show the relationship between the pairs
# first setting the colors dictionary for a nice tidy output
colors = {'Iris-setosa':'g','Iris-virginica':'b','Iris-versicolor':'r'}
# creating a figure and axis
fig, ax = plt.subplots()
# plot the diff data points
for i in range(len(iris_feat['sepallength'])): #this puts limits in place
    plt.scatter(iris_feat['sepallength'][i], iris_feat['sepalwidth'][i],color=colors[iris_species[i]])
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
ax.set_title('Sepal Length vs Width')
ax.legend()
plt.show()

colors = {'Iris-setosa':'c','Iris-virginica':'m','Iris-versicolor':'#E59523'}
fig, ax = plt.subplots()
for i in range(len(iris_feat['petallength'])):
    plt.scatter(iris_feat['petallength'][i], iris_feat['petalwidth'][i],color=colors[iris_species[i]])
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')
ax.set_title('Petal Length vs Width')
ax.legend()
plt.show()

#the below seaborn plot showcases the relationship between the two variables and highlights their distributions
sns.jointplot(x='sepallength', y='sepalwidth', color='#9E23E5', kind='hex', data=iris, space=0) 
plt.show()