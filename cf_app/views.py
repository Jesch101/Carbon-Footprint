from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .forms import CarDetailsForm
from .models import Car, CarMake, CarModel, CarYear

#def index(request):
#    context = {}
#    context['form'] = CarDetailsForm()
#    if request.GET:
#        make = request.GET['car_make']
#        model = request.GET['car_model']
#        year = request.GET['car_year']
#
#        #API data fetch
#        url = "http://localhost:8080/" + "carbonfootprint?car_make=" + make + "&car_model=" + model + "&car_year=" + year
#    return render(request, 'cf_app/index.html', context)

class CarListView(ListView):
    model = Car
    context_object_name = 'car'

class CarCreateView(CreateView):
    model = Car
    form_class = CarDetailsForm
    success_url = reverse_lazy('car_changelist')
    def form_valid(self, form):
        return super().form_valid(form)

# Work in progress. Meant to handle the request data to be used for calculations
# Issue atm is with getting redirects to work with how urls.py is structured
class ParticularCar(FormMixin, DetailView):
    template_name='car_form.html'
    model = Car
    form_class = CarDetailsForm

    def get_success_url(self):
        return reverse_lazy('car_changelist')

    def get_context_data(self, **kwargs):
        context = super(ParticularCar, self).get_context_data(**kwargs)
        context['form'] = CarDetailsForm(initial={'car': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ParticularCar, self).form_valid(form)
    

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarDetailsForm
    success_url = reverse_lazy('car_changelist')

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
