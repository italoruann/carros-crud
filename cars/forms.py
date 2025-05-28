from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import Car


class CarModelForm(forms.ModelForm):
    year_now = datetime.now().year
    
    class Meta:
        model = Car
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        required_fields = ['model', 'brand', 'factory_year', 'model_year', 'value']
        for field in required_fields:
            self.fields[field].required = True
        
    def clean_model(self):
        model = self.cleaned_data.get('model')
        if model is not None:
            if len(model) < 3:
                self.add_error('model', 'O modelo deve ter mais de 3 caracteres.')
        return model
    
    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        if plate:  # Isso cobre tanto None quanto string vazia
            if len(plate) != 7:
                raise ValidationError('A placa precisa ter exatamente 7 caracteres.')
        return plate
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None:
            if value < 20000:
                self.add_error('value', 'O preço deve ser maior que R$ 20.000.')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year is not None:
            if factory_year < 1975:
                self.add_error('factory_year', 'O ano de fabricação deve ser maior que 1975.')
            elif factory_year > self.year_now:
                self.add_error('factory_year', 'O ano de fabricação não pode ser maior que o ano atual.')
                
        return factory_year
    
    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        if model_year is not None:
            if model_year < 1975:
                self.add_error('model_year', 'O ano do modelo deve ser maior que 1975.')
            elif model_year > self.year_now:
                self.add_error('model_year', 'O ano do modelo não pode ser maior que o ano atual.')
            
        return model_year