from django.urls import path, re_path

from . import views

app_name = 'cf_app'

urlpatterns = [
    path('', views.index, name='index'),

]