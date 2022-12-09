from django.contrib import admin

# Register your models here.
from . models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
	search_fields = ('email','uid','username')
	list_display = ('username','email','uid','is_superuser')
	ordering = ('date_joined',)

admin.site.register(CustomUser,CustomUserAdmin)