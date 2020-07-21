from django import forms
from .models import Reminders 
    
class CreateReminderForm(forms.ModelForm):
    
    class Meta:
        model = Reminders
        fields = ["title", "message", "delivery_time"]
                  

       

            