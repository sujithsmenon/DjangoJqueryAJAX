from .models import Friend
from django import forms
import datetime


class DataForm (forms.ModelForm):
    dob = forms.DateField (
        label='What is your birth date?',
        # change the range of the years from 1980 to currentYear - 5
        widget=forms.SelectDateWidget (years=range (1980, datetime.date.today ().year - 5))
    )

    def __init__(self, *args, **kwargs):
        super (DataForm, self).__init__ (*args, **kwargs)

        for name in self.fields.keys ():
            self.fields[name].widget.attrs.update ({
                'class': 'form-control',
            })

    class Meta:
        model = Friend
        fields = ("__all__")