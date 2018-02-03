import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

def bootstrap(statistic_func, iterations, data):
	samples = np.random.choice(data,replace = True, size = [iterations, len(data)])
	#print samples.shape
	data_mean = data.mean()
	vals = []
	for sample in samples:
		sta = statistic_func(sample)
		#print sta
		vals.append(sta)
	b = np.array(vals)
	#print b
	lower, upper = np.percentile(b,[2.5, 97.5])
	return data_mean, lower,upper

if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	#print df.columns
	
	data = df.values.T[0] #getting the values from current fleet 
	boots = []
	boots = bootstrap(np.std,10000,data)
	print("current fleet stander: ",boots[0])
	print("lower bound: ",boots[1])
	print("upper bound: ",boots[2])

	data = df.values.T[1] #getting the values from new fleet 
	data = data[np.logical_not(np.isnan(data))] #remove the nan
	boots = []
	boots = bootstrap(np.std,10000,data)
	print("new fleet stander: ",boots[0])
	print("lower bound: ",boots[1])
	print("upper bound: ",boots[2])

	sns.





	

