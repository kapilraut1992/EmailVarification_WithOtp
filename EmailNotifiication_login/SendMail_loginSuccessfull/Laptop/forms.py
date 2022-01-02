from django import forms
from .models import Laptop


class LaptopForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields='__all__'
        labels={
            'company':'Enter Company Name',
            'model_name':'Enter Laptop Model Name',
            'ram':'RAM (GB)',
            'rom':'ROM(GB)',
            'weight':'Weight(in Kg)'
        }


        def clean_ram(self):
            ram=self.cleaned_data['ram']
            if ram<=0:
                raise forms.ValidationError('RAM must be greater than zero')
            elif ram%2!=0:
                raise forms.ValidationError('Invalide RAM Configuration,it must be Even')
            else:
                return rom

        def clean_rom(self):
            rom = self.cleaned_data['rom']
            if rom <= 0:
                raise forms.ValidationError('ROM must be greater than zero')
            elif ram%2!=0:
                raise forms.ValidationError('Invalide RAM Configuration,it must be Even')
            else:
                return rom

        def clean_weight(self):
            weight = self.cleaned_data['weight']
            if weight <= 0:
                raise forms.ValidationError('Weight must be greater than zero')
            else:
                return weight