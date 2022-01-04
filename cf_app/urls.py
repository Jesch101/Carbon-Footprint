from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home_view'),
    path('add/', views.search_car, name='car_add'),
    path('calculator', views.basic_calc, name='calculator'),
    path('ajax/load-makes/', views.load_makes, name='ajax_load_makes'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),
]