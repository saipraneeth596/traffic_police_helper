from django.contrib import admin
from .models import violation
from .models import vehicleinfo
# Register your models here.
@admin.register(violation)
class UserAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number','violation_done','fine_amt','violation_date')

@admin.register(vehicleinfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'registration_number','owner','make','colour','purchage_date')