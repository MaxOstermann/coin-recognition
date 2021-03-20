from django.db import models


class Image(models.Model):
    width = models.IntegerField(verbose_name="ширина", )
    height = models.IntegerField(verbose_name="высота", )
    middle_color = models.CharField(
        max_length=20,
        verbose_name="средний цвет картинки", )
    coin_num = models.IntegerField(
        verbose_name="количество монет на подложке", )
    coin_sum = models.IntegerField(
        verbose_name="сумма значений монет на подложке", )

# Create your models here.
