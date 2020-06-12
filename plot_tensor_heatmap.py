import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

sns.set()

def plot_tensor_heatmap(x,d,k,label=False):
	''' Plot a heatmap of a vector that has the same structure as a truncated 
	signature, that is which is a sum of tensors k+1 tensors of order 1 up to 
	k+1 in R^d.

	Parameters
	----------
	x: array, shape (n_points,)
		Array that is to be plotted. We must have n_points=(d^(k+1)-1)/(d-1)

	d: int
		Dimension of the underlying space.

	k: int
		Truncation order of a signature corresponding to x.

	label: boolean, default=False
		If label=True, the labels of the signature coeffifients are plotted on 
		the heatmap.
	'''

	mat_coef=np.zeros((k+1,d**k))
	mask=np.zeros((k+1,d**k))
	annot=np.full((k+1,d**k),"",dtype='U256')
	count=0
	for j in range(k+1):
		mat_coef[j,:d**j]=x[count:count+d**j]
		mask[j,d**j:]=True
		inner_count=0
		for label in itertools.product(np.arange(d)+1,repeat=j):
			annot[j,inner_count]=str(label)
			inner_count+=1
		count+=d**j
	with sns.axes_style("white"):
		f, ax = plt.subplots()
		if label:
			ax = sns.heatmap(mat_coef, mask=mask, vmax=.3,xticklabels=False,
                       center=0,cbar_kws={"orientation": "horizontal"})		
		else:
			ax = sns.heatmap(
				mat_coef, mask=mask,xticklabels=False,center=0,
				cbar_kws={"orientation": "horizontal"},annot=annot,fmt='',
				annot_kws={"size": 5})
	plt.show()





