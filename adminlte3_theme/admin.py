from django.contrib import admin
from .models import confrence

class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','city','roll')
    
admin.site.register(confrence,AuthorAdmin)

# Register your models here.
