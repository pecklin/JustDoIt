from encodings import search_function
from django.contrib import admin
# from jmespath import search
from .models import Daily
# Register your models here.

class DailyAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Daily, DailyAdmin)