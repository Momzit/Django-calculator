from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from .pieChart import plotPieChart

from calculator.forms import Inputform
from calculator.models import Input
import os

def repaymentCalculator(P, d, b, r):
	A = P - d 
	r = (r/100)
	n = 12
	numerator = A*(r/n)
	denomenator = 1 - (1 + (r/n))**(-n*b)
	mortgage = (numerator/denomenator)
	return mortgage

def inputform(request):
	os.chdir(os.path.dirname(__file__))
	if request.method == 'POST':
		form = Inputform(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name_to_save']
			purchase = form.cleaned_data['purchase_price']
			deposit = form.cleaned_data['deposit_paid']
			bond = form.cleaned_data['bond_term']
			rate = form.cleaned_data['fixed_interest_rate']
			store = form.save(commit=False)
			store.save()
			monthlyPayment = repaymentCalculator(purchase, deposit, bond, rate)	
			graph = plotPieChart(purchase, deposit, monthlyPayment, bond)
			graph = graph.replace('static\\','')
			
			args = {'form':form, 'purchase': purchase, 'deposit': deposit, 'total':'{0:.2f}'.format(monthlyPayment), 'bond':bond, 'rate':rate, 'graph':graph}
			return render(request, 'calculator/inputform.html', args)
	else:
		form = Inputform()
	return render(request, 'calculator/inputform.html', {'form': form})


class ShowResults(generic.DetailView):
	model = Input
	template_name = 'calculator/results.html'

	
class PrevResults(generic.ListView):
	context_object_name = 'Previous_results'
	template_name = 'calculator/index.html'

	def get_queryset(self):
		return Input.objects.all()
