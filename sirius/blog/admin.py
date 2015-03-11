from django.contrib import admin
from models import Categoria, Post

class AutoSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Categoria)
admin.site.register(Post, AutoSlug)