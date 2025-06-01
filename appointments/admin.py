from django.contrib import admin
from .models import Doctor,Patient

# admin.site.register(Doctor)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')  # نمایش توی جدول ادمین
    search_fields = ('name', 'specialty')  
    

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "national_id", "phone_number", "created_at")
    search_fields = ("first_name", "last_name", "national_id")
    list_filter = ("created_at",)