# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render

from .models import Credito,TMC

# Create your views here.

def detail(request):
	latest_tmc_list = TMC.objects.order_by('-fecha_consulta)[:10]
	template = loader.get_template('tmc/index.html')
	context = {
		'Últimas consultas de TMC': latest_tmc_list
	}
	return HttpResponse(template.render(context,request))
