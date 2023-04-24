#pandas will be used to output the summaries into a single text file
import pandas as pd
#numpy will also be called to access the np attributes and evaluate some maths
import numpy as np
from numpy import random
#and finally, matplotlib will be used to save a histogram and display a scatterplot
import matplotlib.pyplot as plt
'''firstly, the data will be called in and displayed using pandas,
 and then output to a text file'''


Iris = pd.read_csv("iris_csv.csv")
print(Iris.shape)
print(Iris.describe())

np.savetxt(Iris.txt, Iris.describe)

'''






#i also want to analyse the mean, min and max values of this data
#pd.DataFrame(filename)
#print(df)
with open(Iris):
    describe()'''
Iris.groupby('class').agg(['mean','median','max','min'])
Iris.groupby('class').agg([np.mean, np.median, np.max, np.min])
print(Iris.groupby)

#the code for making the histogram which saves to png
'''
x = random.normal(loc = 5, scale = 2, size=(1000))
plt.hist(x, color="c")
plt.show()'''