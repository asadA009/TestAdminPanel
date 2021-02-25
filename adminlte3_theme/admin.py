from django.contrib import admin
from .models import confrence

class AuthorAdmin(admin.ModelAdmin):
    list_display=('id','confrence_ID','date','venu','image','confrence_Overview','register','travel_information')
    
admin.site.register(confrence,AuthorAdmin)

