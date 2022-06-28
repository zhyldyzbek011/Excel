from django.contrib import admin
from excel.models import Month, Statistic, Date
from django.contrib import admin

admin.site.register(Date)
admin.site.register(Month)
admin.site.register(Statistic)
