from django.db import models

# Create your models here.
class Verify(models.Model):
    name = models.CharField(max_length=32, verbose_name="好友用户名")
    sex = models.CharField(max_length=32, verbose_name="用户性别")
    age = models.CharField(max_length=32, verbose_name="用户年龄")
    def __str__(self):
        return self.name
