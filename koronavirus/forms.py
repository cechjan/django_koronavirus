from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Stat


class StatModelForm(ModelForm):
    def clean_pocet_obyvatel(self):
        data = self.cleaned_data['pocet_obyvatel']
        self.obyvatele_rozloha(data, 'Nepltaný počet obyvatel')
        return data

    def clean_rozloha(self):
        data = self.cleaned_data['rozloha']
        self.obyvatele_rozloha(data, 'Neplatná rozloha')
        return data

    @staticmethod
    def obyvatele_rozloha(data, error):
        if data <= 0:
            raise ValidationError(error)

    class Meta:
        model = Stat
        fields = ['nazev_statu', 'zkratka_statu', 'vlajka', 'forma_statu', 'pocet_obyvatel', 'rozloha', 'text']
        labels = {'nazev_statu': 'Název státu', 'zkratka_statu': 'Zkratka státu', 'vlajka': 'Obrázek vlajky',
                  'forma_statu': 'Forma státu', 'pocet_obyvatel': 'Počet obyvatel',
                  'rozloha': 'Rozloha (v kilometrech čtverečních)', 'text': "O státu"}
