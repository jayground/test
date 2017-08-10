from django.shortcuts import render
from django.views.generic.list import ListView

from estimate.models import Estimate

class EstimateList(ListView):
	model = Estimate