from django import forms
from .models import Reminders 

from django.contrib.admin.widgets import AdminDateWidget
class CreateReminderForm(forms.ModelForm):
    
    class Meta:
        model = Reminders
        fields = ["title", "message", "delivery_time"]
        #temporary place holder to be replaced with datetime picker
        widgets = {
            'delivery_time': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
        }
