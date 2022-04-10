from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'recommended_by', 'updated', 'created')


admin.site.register(Profile, ProfileAdmin)
