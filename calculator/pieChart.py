import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, time, glob

def plotPieChart(purchase, deposit, monthly_repay, n):
	loan_amount = purchase - deposit
	total_loan_payment = monthly_repay*n*12
	total_interest = total_loan_payment - loan_amount

	fig, ax = plt.subplots(figsize=(6,3), subplot_kw=dict(aspect='equal'))
	labels = ["Monthly repayments \n R{0:.2f}".format(monthly_repay),
				"Loan amount \n R{0:.2f}".format(loan_amount),
				"Total interest \n R{0:.2f}".format(total_interest),
				"Total loan payment \n R{0:.2f}".format(total_loan_payment)]
	data = [monthly_repay, loan_amount, total_interest, total_loan_payment]
	wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

	bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
	kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

	for i, p in enumerate(wedges):
		ang = (p.theta2 - p.theta1)/2. + p.theta1
		y = np.sin(np.deg2rad(ang))
		x = np.cos(np.deg2rad(ang))
		horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
		connectionstyle = "angle,angleA=0,angleB={}".format(ang)
		kw["arrowprops"].update({"connectionstyle": connectionstyle})
		ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
	
	
	if not os.path.isdir('static'):
		os.mkdir('static')
	else:
		for filename in glob.glob(os.path.join('static', '*.png')):
			os.remove(filename)

	plotfile = os.path.join('static', "PieChart" + '.png')
	plt.savefig(plotfile)
	return plotfile
if __name__ == '__main__':
	graph = plotPieChart(380000, 76000, 1969.23, 30)
	print(graph[7:])

