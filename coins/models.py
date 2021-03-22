from django.db import models
from coins.utils import get_middle_color


class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    width = models.IntegerField(verbose_name="ширина", blank=True, null=True)
    height = models.IntegerField(verbose_name="высота", blank=True, null=True )
    middle_color = models.CharField(
        max_length=20,
        verbose_name="средний цвет картинки", blank=True, null=True )
    coin_num = models.IntegerField(
        verbose_name="количество монет на подложке", blank=True, null=True )
    coin_sum = models.IntegerField(
        verbose_name="сумма значений монет на подложке", blank=True, null=True )

    @classmethod
    def create(cls, image):
        image_obj = cls(image=image)
        image_obj.width = image_obj.width
        image_obj.height = image_obj.height
        image_obj.middle_color = get_middle_color(image_path=image_obj.image.url)
        image_obj.save()
        # do something with the book
        return image_obj

# Create your models here.
