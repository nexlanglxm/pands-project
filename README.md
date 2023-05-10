# pands-project
This is the readme file for the final project in the Programming and Scripting module
The project is concerned with the well-known **Fisher's Iris data set**

Fisher's Iris data set, also known as the **Iris flower data set**, is a dataset that records the length and width measurements for sepals and petals for three distinct Iris species: *Iris setosa*, *Iris virginica* and *Iris versicolor*.
It is considered the best known database in pattern recognition literature according to (Dua and Graff, 2019), and is likened to the "Hello World" of Data Analysis (GeeksforGeeks, 2020b).



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
I spent a large amount of time reading online resources such as GeeksforGeeks (GeeksforGeeks, 2020) and AskPython (Verma, 2020), and playing with the different ways of outputting the data.
Initially I had problems with trying to get the file to read properly, and this was remedied with some kind advice from Andrew and the usage of relative file paths.
Then I had to deal with the problems of trying to output column headings onto the dataset and encountering the 0 index issue.

Following this, I elected to use a file which I got online (Pradhan, 2022) which already had the columns in place as I realised I was wasting a large amount of time on something of little relative importance.

I then spent a while playing around trying to get numPy to output the summary into a single text file.

I actually found the iloc feature when browsing solutions regarding datasets (Rastogi, 2021) and it proved to be of much use to me and might have also made it possible to use the original dataset, good to know, and might go back and change that once I make more significant progress in other aspects. 
This did lead me to successful creation of my histograms and scatterplots, now to get the different variables to output.

I managed to get a histogram output going to a png file in the way desired with help from the information on (Welch, n.d.). 
I went back and played around with the min(),max() and mean() keyword arguments to get the code to output numeric only values, and then began again working towards outputting these values into the text file.

When I got some success using the numPy savetxt method, I discovered by reading the file on the numPy manual (numpy.org, n.d.) that the input would need to be an array, which I would then need to compile all of these into a single output..
After some playing with the savetxt, I elected to create different files to overcome the aforementioned issues with the array/tuple that was being created.

After outputting mean semi-successfully to a png file, I am not sure it is the most meaningful to output.. or at least in the fashion that I have done so. I will explore further. 
To get a more useful output, I need to differentiate the mean values, and output the mean values of certain features for each different species of iris. To do this I will call in the species and output different values according to the features

With the successful creation of the scatterplots outputting pairs of variables, and the different values going to their respective positions correctly, I look towards possibly using some Seaborn outputs to create a few neat looking outputs




References.
