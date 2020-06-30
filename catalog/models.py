from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey

class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Market(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    city = models.ForeignKey(City, related_name='markets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Category(MPTTModel):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    parent = TreeForeignKey('self', blank=True, null=True,
                            related_name='children', db_index=True, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=12, blank=True, null=True)
    old_price = models.DecimalField('Старая Цена', decimal_places=2, max_digits=12, blank=True, null=True)
    img = models.ImageField(max_length=250,upload_to='products/')
    composition = models.TextField(blank=True)
    producer = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_title(self):
        return self.name

    def get_absolute_url(self):
        return "/categories/{}_{}.html".format(self.slug,self.pk)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
