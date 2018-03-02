import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, time, glob

def bargraph(purchase, bond, monthly):
	monthly_payments = monthly
	i = monthly_payments
	bond_term = bond
	N = bond_term*12
	A = [monthly_payments]
	for x in np.arange(1,N):
		monthly_payments += i
		A.append(monthly_payments)


	ind = np.arange(N)    # the x locations for the groups
	width = 0.35       # the width of the bars: can also be len(x) sequence

	plt.figure()
	p1 = plt.bar(ind, A, width, label='monthly_payments')
	# p2 = plt.bar(ind, womenMeans, width,
             # bottom=menMeans, yerr=womenStd)

	plt.ylabel('monthly_payments')
	plt.xlabel('Months')
	plt.title('Repayments for the term')
	# plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
	# plt.yticks(np.arange(0, 81, 10))
	plt.legend(loc='upper left')
	if not os.path.isdir('static'):
		os.mkdir('static')
	else:
		for filename in glob.glob(os.path.join('static', '*.png')):
			os.remove(filename)

	plotfile = os.path.join('static', str(time.time()) + '.png')
	plt.savefig(plotfile)
	return plotfile
if __name__ == '__main__':
	print(bargraph(1000, 12, 20))
