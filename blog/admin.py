from django.contrib import admin
from .models import BlogType, Blog
admin.site.site_header = '聪明蛋的个人学习小站后台'  # 设置header
admin.site.site_title = '聪明蛋的个人学习小站后台'  # 设置title
admin.site.index_title = '聪明蛋的个人学习小站后台'


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'author', 'get_read_num', 'created_time', 'last_updated_time')


