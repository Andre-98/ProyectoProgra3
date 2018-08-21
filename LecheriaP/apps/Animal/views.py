# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.shortcuts import render, redirect

from django.http import HttpResponse

from apps.Animal.forms import AnimalForm

# Create your views here.

def index(request):
	return render(request, 'Animal/index.html')


def Animal_view(request):
	if request.method == 'POST':
		form = AnimalForm(request.POST)
		if form.is_valid():
			form.save()
	 	return redirect('Animal:index')
	else:
		form = AnimalForm()
	return render(request, 'Animal/Animal_form.html', {'form':form})
