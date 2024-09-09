from django import forms
from .models import event_details
class eventform(forms.ModelForm):
    class Meta:
        model = event_details
        fields = ('event_name', 'event_date','event_time', 'event_desp', 'event_image')
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'type': 'time'}),
        }