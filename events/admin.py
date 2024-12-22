from django.contrib import admin
from .models import Events,Event_SignUp
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
    
# Register your models here.

admin.site.register(Event_SignUp)



# admin.site.register(Products)

class EventItemInLine(admin.StackedInline):
    model = Event_SignUp
    fields = ['name','last_name','category','phone_number','Id_pic','insurance_pic']
    extra = 1
@admin.register(Events)
class EventAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ['title','date','date_time_created','status']
    inlines =[
        EventItemInLine,
    ]




