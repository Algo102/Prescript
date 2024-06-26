from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db import models as m


# from django.contrib.auth.models import User


# class Category(m.Model):
#     name = m.CharField(max_length=100)
#     description = m.TextField(default='', blank=True)
#     photo = m.ImageField(upload_to='category_photos', blank=True, null=True)
#
#     def __str__(self):
#         return f"Категория: {self.name}, Описание: {self.description}, Фото: {self.photo}"
#
#     class Meta:
#         verbose_name = "Категория"
#         verbose_name_plural = "Категории"



# class Receipt(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     description = models.TextField(default='', blank=True)
#     steps = models.TextField()
#     time = models.IntegerField()
#     photo = models.ImageField(upload_to='receipt_photos/', blank=True, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return not (f'Here is your receipt for {self.name} from {self.category}. '
#                     f'Please be aware you will need about {self.time} minutes. So, follow this steps {self.steps}')

