from django.contrib import admin
from .models import Drone,Medication,Loads, EnventLog 
# Register your models here.


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    fields = ['serial_number','model','weight_limit','battery_capacity', 'state']
    list_display = ['id','serial_number','model','weight_limit','battery_capacity', 'state']
    search_fields = ['serial_number','model', 'state']



@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display= ['id','name','weight', 'code','image']
    search_fields = ['name','weight', 'code']


@admin.register(Loads)
class LoadsAdmin(admin.ModelAdmin):
    list_display = ['id','drone', 'medication']
    search_fields = ['drone', 'medication']



@admin.register(EnventLog)
class EventLogAdmin(admin.ModelAdmin):
    list_display = ['date_checked','drone','battery']
    search_fields = ['drone']