from django import forms
from datetime import datetime

# TODO: Populate these dictionaries with api calls (?) for US makes/models/year
# Ex: 
#   Make: BMW
#   Mode: 1 Series
#   Year: 2013
makes = (
    ("BMW", "BMW"),
    ("Toyota", "Toyota"),
    ("Nissan", "Nissan"),
    ("Ford", "Ford"),
    ("Mustang", "Mustang"),
)

models = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

class CarDetailsForm(forms.Form):
    car_make = forms.ChoiceField(choices=makes)
    car_model = forms.ChoiceField(choices=models)
    car_year = forms.DecimalField(max_value=datetime.now().year, min_value=2000)