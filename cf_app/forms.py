from django import forms
from cf_app.models import Car, CarMake, CarModel, CarYear

class CarDetailsForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['year', 'make', 'model']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].queryset = CarYear.objects.order_by('year')
        self.fields['make'].queryset = CarMake.objects.none()
        
        if 'year' in self.data:
            try:
                year_id = int(self.data.get('year'))
                self.fields['make'].queryset = CarMake.objects.filter(year_id=year_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['make'].queryset = self.instance.year.make_set.order_by('year')

        self.fields['model'].queryset = CarMake.objects.none()

        if 'make' in self.data:
            try:
                make_id = int(self.data.get('make'))
                self.fields['model'].queryset = CarModel.objects.filter(make_id=make_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            
            self.fields['model'].queryset = self.instance.make.model_set.order_by('name')

