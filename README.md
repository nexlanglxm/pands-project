# pands-project
This is the readme file for the final project in the Programming and Scripting module
The project is concerned with the well-known **Fisher's Iris data set**

Fisher's Iris data set, also known as the **Iris flower data set**, is a dataset that records the length and width measurements for sepals and petals for three distinct Iris species: *Iris setosa*, *Iris virginica* and *Iris versicolor*.




1. Research the data set online and write a summary about it in your README. - Week of **April 10th**
2. Download the data set and add it to your repository.                      - Week of **April 10th**
3. Write a program called analysis.py that:
    1. Outputs a summary of each variable to a single text file,             - Week of **April 17th**
    2. Saves a histogram of each variable to png files, and                  - Week of **April 17th**
    3. Outputs a scatter plot of each pair of variables.                     - Week of **April 24th**
    4. Performs any other analysis you think is appropriate


My understanding of outputting a summary of the variables is getting things like the mean, standard deviation, mode, median, min or max values given a set of data.
Of course, some of these would be better used in certain data types, and given these are tiny measurements taken from subspecies of flowers; I think min, max, mean and median values would be of somewhat importance.

Firstly I must get the data set to output to a txt file. So there was a large amount of work for me in trying to get pandas to work. Although it was not a requirement(pandas), I believe it will work out in my favour, given some time and practice.
I spent a large amount of time reading online resources such as GeeksforGeeks and AskPython, and playing with the different ways of outputting the data.
Initially I had problems with trying to get the file to read properly, and this was remedied with some kind advice from Andrew and the usage of relative file paths.
Then I had to deal with the problems of trying to output column headings onto the dataset and encountering the 0 index issue.

Following this, I elected to use a file which I got online (@ this link https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset) which already had the columns in place as I realised I was wasting a large amount of time on something of little relative importance.

I then spent a while playing around trying to get numPy to output the summary into a single text file.

I actually found the iloc feature when browsing solutions regarding datasets (https://www.analyticsvidhya.com/blog/2021/06/guide-to-data-visualization-with-python-part-1/) and it proved to be of much use to me and might have also made it possible to use the original dataset, good to know, and might go back and change that once I make more significant progress in other aspects. 
This did lead me to successful creation of my histgrams and scatterplots, now to get the different variables to output.

I managed to get a histogram output going to a png file in the way desired. 
I went back and played around with the min(),max() and mean() keyword arguments to get the code to output numeric only values, and then began again working towards outputting these values into the text file.

When I got some success using the numPy savetxt method, I discovered by reading the file on the numPy manual (numpy.org, n.d.) that the input would need to be an array, which I would then need to compile all of these into a single output..
After some playing with the savetxt, I elected to create different files to overcome the aforementioned issues with the array/tuple that was being created.


After outputting mean semi-successfully to a png file, I am not sure it is the most meaningful to output.. or at least in the fashion that I have done so. I will explore further. 
To get a more useful output, I need to differentiate the mean values, and output the mean values of certain features for each different species of iris. To do this I will call in the species and output different values according to the features





References.

https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 - Information concerning the data set

https://www.askpython.com/python/examples/calculate-summary-statistics - how to calculate summary stats

https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/ - Saving files using matplotlib

https://learnpython.com/blog/how-to-summarize-data-in-python/ - Data summaries in Python

GeeksforGeeks. (2020). Add column names to dataframe in Pandas. [online] Available at: https://www.geeksforgeeks.org/add-column-names-to-dataframe-in-pandas/ [Accessed 20 Apr. 2023]

.Kumar, A. (2023). Pandas Dataframe: How to Add Rows & Columns. [online] Data Analytics. Available at: https://vitalflux.com/pandas-dataframe-how-to-add-rows-columns/ [Accessed 24 Apr. 2023].

numpy.org. (n.d.). numpy.savetxt — NumPy v1.22 Manual. [online] Available at: https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html.

Pydata.org. (2019). pandas.read_csv — pandas 0.25.3+0.g43013d49f.dirty documentation. [online] Available at: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html.Python, - How to use CSV with Pandas

R. (n.d.). pandas Sort: Your Guide to Sorting Data in Python – Real Python. [online] realpython.com. Available at: https://realpython.com/pandas-sort-python/#using-column-labels-to-sort [Accessed 20 Apr. 2023].

Verma, J. (2020). How to Calculate Summary Statistics in Python? - AskPython. [online] How to calculate summary statistics in Python? - AskPython. Available at: https://www.askpython.com/python/examples/calculate-summary-statistics 