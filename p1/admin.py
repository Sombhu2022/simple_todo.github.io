from django.contrib import admin
from .models import curd

# Register your models here.
#class MemberAdmin(admin.ModelAdmin):

#	list_display=("name","email","phone")
admin.site.register(curd)