from django.contrib import admin
from excel.models import Month, Statistic, Date, Table_1, Table_2, Date_1
from django.contrib import admin

admin.site.register(Date)
admin.site.register(Month)
admin.site.register(Statistic)
admin.site.register(Date_1)
admin.site.register(Table_1)
admin.site.register(Table_2)
