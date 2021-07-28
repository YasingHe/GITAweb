from django.contrib import admin
from .models import Article,Messages,Tag,Notice
# Register your models here.
admin.site.site_header = '天河信息社管理后台'
admin.site.site_title = '天河信息社管理'

class ArticleAdmin(admin.ModelAdmin):
    # pk:索引
    # 属性list_display表示要显示哪些属性
    list_display = ['pk','title','data_added']

admin.site.register(Article,ArticleAdmin)

admin.site.register(Messages)
admin.site.register(Tag)
admin.site.register(Notice)