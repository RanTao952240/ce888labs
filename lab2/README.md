# Lab2

## Overleaf

Overleaf is an online latex typesetting system. You will need it to create the project for this module. 

Go to [www.overleaf.com](https://www.overleaf.com) and create an account and a new document.

## Setting up 
* Do the following from the unix prompt of your VM
	* Go to the directory you "cloned" the module files last time
	* Do `git pull origin master' to bring the new files

* Do the following tasks using your windows share or your unix account in the VM	
	* Copy the lab files from the module directory into your own github lab directory, in "lab2" folder
	* Remove everything from the copied README.md

## Histogram and Scaterplot

A business is looking at changing their current vehicle fleet and replacing their vehicles with ones used by their competitors. They are have captured the MPG of some of the cars in both fleets fleets.


1. Read the data for the vehicles found in the file `vehicles.csv`
2. Create histograms and scatterplots for "current fleet" and "proposed fleet" - see `salaries.py` on how to do this

![scaterplot](./scaterplot.png?raw=true)

## Standard deviation comparison via the boostrap

The business analysts come up a super-complicated comparison algorithm that requires the standard deviation bounds to in order to say which fleet is better. 

- [ ] Find the standard deviation of both samples


Use the example code for the bootstrap provided in ``bootstrap.py'' to do the following
- [ ] Find the upper and lower bound of the standard deviation of the current fleet
- [ ] Do the same with the new fleet
- [ ] Are the standard deviations comparable? 

## Present the analysis
- [ ] Write a very small text on what you did in your README.md. Include the generated plots as below 

* Part one:
        
           1.using  the file of vehicles.csv and using dropna() to discard missing(nan) data
 
           2.using seaborn function to produce histogram and scaterplot and using numpy function
           to canculate Mean, Median, Var and Mad
           
	   Mean: 30.48
	   Median: 32.00
	   Var: 36.83
	   Mad: 4.00
Histogram
![histogram](./partone_histogram.png?raw=true)

Scaterplot
![scaterplot](./partone_scaterplot.png?raw=true)

* Part two:
           Because using bootstrap to predict the data, so deviding values into two rows and predict each boinds
	   
	   For Current fleet:
                             stander: 20.14
			     lower bound: 5.80
			     upper bound: 6.94
	   For New fleet:
                             stander: 30.48
			     lower bound: 5.14
			     upper bound: 6.92     
	   
	   
	  


- [ ] Write a very small text description of the analysis in overleaf, download the pdf and put in in github alongside the rest of your lab2 

(The data is from a Japanese vs American cars MPG comparison I found online in a stat book - can't find it again though!)

- [ ] Once you are done, save your changes in github
	* Go inside your lab directory and do 
      * ``git add -A -v``
      * ``git commit -m <message>``
      * ``git push origin master``
