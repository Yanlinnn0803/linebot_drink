from django.contrib import admin

# Register your models here.
from drinkbotapp.models import *

class Client_Info_Admin(admin.ModelAdmin):
    list_display = ('cName', 'cUid','mdt')

admin.site.register(Client_Info, Client_Info_Admin)
admin.site.register(Client_History)