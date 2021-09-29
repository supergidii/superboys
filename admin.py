from django.contrib import admin
from . models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number','date_joined')
    search_fields = ['username']
    ordering = ['username']
    readonly_fields=('date_joined', 'last_login')
    
admin.site.register(Profile,ProfileAdmin)
