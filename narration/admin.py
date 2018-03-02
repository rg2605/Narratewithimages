from django.contrib import admin
from .models import Images, Content
# Register your models here.

#class ImageInline(admin.TabularInline):
 #   model = Images
  #  extra = 3

#class ImageAdmin(admin.ModelAdmin):
 #   inlines = [ ImageInline, ]

admin.site.register(Images)
admin.site.register(Content)