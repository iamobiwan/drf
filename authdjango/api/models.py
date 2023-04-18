from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField("Категория", max_length=150)
    

    def __str__(self):
        return self.name
    

class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField("Наименование", max_length=100)
    price = models.PositiveIntegerField("Цена", default=0)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



