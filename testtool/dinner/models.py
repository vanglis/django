from django.db import models

# Create your models here.
from django.db import models

class Dinner(models.Model):

    foods_name = models.CharField(u'菜名',max_length=20)
    TYPE_CHOICES = (
        (u'冷菜', u'冷菜'),
        (u'热炒菜', u'热炒菜'),
        (u'干锅类', u'干锅类'),
        (u'锅仔类', u'锅仔类'),
        (u'汤类', u'汤类'),
    )
    foods_type = models.CharField(u'菜品类型', max_length=20,choices=TYPE_CHOICES)
    price = models.DecimalField(u'价格',max_digits=10,decimal_places=2)
    add_time = models.DateTimeField(u'添加时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __str__(self):
        return u'%s %s %s' % (self.foods_name, self.foods_type, self.price)

    class Meta:
        verbose_name = '菜单' #提供自述名显示
        verbose_name_plural = '菜单' #自述名复述形式
        ordering = ['-add_time']

    def save(self, *args, **kwargs):
        super(self.__class__, self).save(*args, ** kwargs) #将数据写入数据库
        return 

class TakeOrder(models.Model):

    foods_name = models.CharField(u'菜名',max_length=20)
    TYPE_CHOICES = (
        (u'冷菜', u'冷菜'),
        (u'热炒菜', u'热炒菜'),
        (u'干锅类', u'干锅类'),
        (u'锅仔类', u'锅仔类'),
        (u'汤类', u'汤类'),
    )
    foods_type = models.CharField(u'菜品类型', max_length=20,choices=TYPE_CHOICES)
    price = models.DecimalField(u'价格',max_digits=10,decimal_places=2)
    username = models.CharField(u'点单人姓名', max_length=20)
    add_time = models.DateTimeField(u'添加时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __str__(self):
        return u'%s %s %s' % (self.foods_name, self.foods_type, self.price)

    class Meta:
        verbose_name = '去点菜' #提供自述名显示
        verbose_name_plural = '去点菜' #自述名复述形式
        ordering = ['-add_time']

    def save(self, *args, **kwargs):
        super(self.__class__, self).save(*args, ** kwargs) #将数据写入数据库
        return

