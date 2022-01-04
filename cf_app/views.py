from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q

from .forms import CarDetailsForm
from .models import Car, CarMake, CarModel, CarYear

def index(request):
    context = {}
    #context['form'] = CarDetailsForm()
    return render(request, 'cf_app/home.html', context)

def search_car(request):
    queryset = Car.objects.all()
    form = CarDetailsForm(request.POST)

    if request.method == "POST" and form.is_valid():
        queryset = Car.objects.filter(year__year__exact=form.cleaned_data['year'].year,
                                    make__name__exact=form.cleaned_data['make'].name,
                                    model__name__exact=form.cleaned_data['model'].name)
        context = {
        'year':form.cleaned_data['year'].year,
        'make':form.cleaned_data['make'].name,
        'model':form.cleaned_data['model'].name,
        'form':form,
        'queryset':queryset,
        'fuel_efficiency': queryset[0].fuel_efficiency}
    else:
        context = {
        'form':form,
        'queryset':queryset,
        'fuel_efficiency': False}

    return render(request, 'cf_app/car_form.html', context)

#Basic calculator view
def basic_calc(request):
    context = {}
    return render(request, 'cf_app/basic_calc.html', context)
    
class CarCreateView(CreateView):
    model = Car
    form_class = CarDetailsForm
    success_url = reverse_lazy('home_view')

def load_makes(request):
    year_id = request.GET.get('year')    
    makes = CarMake.objects.filter(year_id=year_id).order_by('name')
    context = {'makes': makes}
    return render(request, 'cf_app/make_dropdown_list.html', context)

def load_models(request):
    make_id = request.GET.get('make')    
    models = CarModel.objects.filter(make_id=make_id).order_by('name')
    context = {'models': models}
    return render(request, 'cf_app/model_ddl.html', context)
