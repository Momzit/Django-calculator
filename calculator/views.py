from django.shortcuts import render, redirect
from django.template import RequestContext

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from .bargraph import bargraph

from calculator.forms import Inputform
from calculator.models import Input
import os

def inputform(request):
	os.chdir(os.path.dirname(__file__))
	total = None
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
			if rate == 0.0:
				bond = 12*bond
				total = purchase/bond
				total = '%.2f' %(total)
				graph = bargraph(store.purchase_price, store.bond_term, total)
				graph = graph.replace('static/','')
			else:
				rate = (rate/12)/100
				rate_2d = '%.2f' %(rate)
				bond = 12*bond
				total = (rate*purchase*(1+rate)**(bond))/((1+rate)**(bond) - 1)
				total = '%.2f' %(total)
				graph = bargraph(store.purchase_price, store.bond_term, total)
				graph = graph.replace('static/','')

			args = {'form':form, 'purchase': purchase, 'deposit': deposit, 'total':total, 'bond':bond, 'rate':rate_2d, 'graph':graph}
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
