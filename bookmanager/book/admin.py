from django.contrib import admin

# Register your models here.

# 导入模型
from book.models import BookInfo,PeopleInfo

# 注册模型
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
