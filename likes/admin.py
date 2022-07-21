from django.contrib import admin
from .models import LikeCount, LikeRecord


@admin.register(LikeCount)
class LikeCountAdmin(admin.ModelAdmin):
    list_display = ('liked_num', 'content_object')


@admin.register(LikeRecord)
class LikeRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'liked_time', 'content_object')


from django.contrib import admin

# Register your models here.
