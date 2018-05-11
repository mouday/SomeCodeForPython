from django.contrib import admin


# Register your models here.
from . import models
class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','content','pub_time')
	list_filter=('pub_time',)
admin.site.register(models.Aticle,ArticleAdmin)