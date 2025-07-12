from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'contact', 'dob', 'user', 'created_at')
    search_fields = ('name', 'contact', 'gender', 'user__username')
    list_filter = ('gender', 'created_at')
