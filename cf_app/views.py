from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CarDetailsForm, BasicInputForm
from .models import Car, CarMake, CarModel

def index(request):
    context = {}
    return render(request, 'cf_app/home.html', context)

def search_car(request):
    queryset = Car.objects.all()
    form = CarDetailsForm(request.POST)

    if request.method == "POST" and form.is_valid():
        queryset = Car.objects.filter(year__year__exact=form.cleaned_data['year'].year,
                                    make__name__exact=form.cleaned_data['make'].name,
                                    model__name__exact=form.cleaned_data['model'].name)
        
        #CO2 Emission Calculation
        mpg = queryset[0].fuel_efficiency
        lbs = 20 #Factor of CO2 for every gallon consumed
        emissions = round(lbs/mpg, 2) #lbs/mile of CO2
        if emissions > 2000:
            emissions = round(emissions/2000) 

        context = {
        'year':form.cleaned_data['year'].year,
        'make':form.cleaned_data['make'].name,
        'model':form.cleaned_data['model'].name,
        'form':form,
        'queryset':queryset,
        'fuel_efficiency': queryset[0].fuel_efficiency,
        'emissions':emissions}

    else:
        context = {
        'form':form,
        'queryset':queryset,
        'fuel_efficiency': False}

    return render(request, 'cf_app/car_form.html', context)

#Basic calculator view
def basic_calc(request):
    context = {}
    form = BasicInputForm()
    context['form'] = form
    if request.POST:
        mpg = int(request.POST['fuel_efficiency'])
        lbs = 20 #Factor of CO2 for every gallon consumed
        emissions = round(lbs/mpg, 2) #lbs/mile of CO2
        if emissions > 2000:
            emissions = round(emissions/2000)
        context = {
            'mpg':mpg,
            'emissions':emissions,
            'form':form
        }
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
