from django.contrib import admin
from .models import Contact,SocialMedia



class ContactAdmin(admin.ModelAdmin):

    list_display = ['phone']
    list_filter = ['phone',]

admin.site.register(Contact,ContactAdmin)

class SocialMediaAdmin(admin.ModelAdmin):

    list_display = ['name']
    list_filter = ['name',]

admin.site.register(SocialMedia,SocialMediaAdmin)
