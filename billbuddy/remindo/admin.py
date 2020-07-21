from django.contrib import admin
from .models import Visits, Reminders

@admin.register(Visits)
class VisitsHistoryAdmin(admin.ModelAdmin):
    #define the view in the admin panel
    list_display = ["time","ip_address"]
    list_filter = ["time"]
     
    def get_visit(self, obj):
        return str(obj.visit)
     
    get_visit.short_description = 'Visits'
    
@admin.register(Reminders)
class RemindersHistoryAdmin(admin.ModelAdmin):
     #define the view in the admin panel
    list_display = ["title","message","delivery_time","sent","receiver","sender"]
    list_filter = ["sent","delivery_time","receiver"]
    
    def get_reminder(self, obj):
        return str(obj.reminder)
    
    get_reminder.short_description = 'Reminders'
       
