#from django.contrib import admin

# Register your models here.
from django.contrib import  admin
from .models import Bb

#admin.site.register(Bb)

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)

admin.site.register(Bb, BbAdmin)