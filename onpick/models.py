from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.category_name

class OnpickYoutube(models.Model):
    onpick_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, models.CASCADE, blank=True, null=True)
    onpick_title = models.CharField(max_length=200, blank=True, null=True)
    onpick_youtube = models.CharField(max_length=200, blank=True, null=True)
    onpick_content = models.CharField(max_length=3000, blank=True, null=True)
    onpick_product = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.onpick_title
