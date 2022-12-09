from django.contrib import admin

# Register your models here.
from activity.models import Activity, SubActivity

admin.site.register(Activity)
admin.site.register(SubActivity)
