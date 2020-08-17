from django.contrib import admin
from details.models import *
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

class DataAdmin(admin.ModelAdmin):
	list_display = ('name','email','subject')
	list_filter = ['created_at']

class News_list(admin.ModelAdmin):
	list_display = ['EMAIL']



admin.site.site_header = 'Manish Admin Page'
admin.site.register(Inquery, DataAdmin)
@admin.register(News)
class Details(ImportExportModelAdmin):
	pass






