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
	print("current fleet stander: ",boots[0])
	print("lower bound: ",boots[1])
	print("upper bound: ",boots[2])

	df_boot = pd.DataFrame(boots,  columns=['Boostrap Iterations','Mean',"Value"])
	sns_plot = sns.lmplot(df_boot.columns[0],df_boot.columns[1], data=df_boot, fit_reg=False,  hue="Value")

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,100000)

	sns_plot.savefig("bootstrap_confidence.png",bbox_inches='tight')
	sns_plot.savefig("bootstrap_confidence.pdf",bbox_inches='tight')

	#print ("Mean: %f")%(np.mean(data))
	#print ("Var: %f")%(np.var(data))




	

