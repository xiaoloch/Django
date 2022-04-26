from django.db import models

# Create your models here.

# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

