#pandas will be used to output the summaries into a single text file
import pandas as pd
#numpy will also be called to access the np attributes and evaluate some maths
import numpy as np
#and finally, matplotlib will be used to save a histogram and display a scatterplot
import matplotlib.pyplot as plt
'''firstly, the data will be called in and displayed using pandas,
 and then output to a text file'''

#filename = 'iris.data'
Iris = pd.read_csv("C:/Users//neilj/pands/pands-project/iris.data")
Iris.info()
Iris
#df.to_frame(iris.txt)











'''i also want to analyse the mean, min and max values of this data'''
#pd.DataFrame(filename)
#print(df)

'''the code for making the histogram which saves to png'''