from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.CarListView.as_view(), name='car_changelist'),
    path('add/', views.CarCreateView.as_view(), name='car_add'),  
    #path('<slug:pk>/', views.ParticularCar.as_view(), name='car_add'),
    path('<str:pk>/', views.CarUpdateView.as_view(), name='car_change'),
    path('ajax/load-makes/', views.load_makes, name='ajax_load_makes'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),
]