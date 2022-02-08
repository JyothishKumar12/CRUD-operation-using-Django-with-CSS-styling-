from django.contrib import admin
from.models import StudntRegistration
# Register your models here.
@admin.register(StudntRegistration)

class studentregisterAdmin(admin.ModelAdmin):
    list_display=[id,'name','email','department','mobno']