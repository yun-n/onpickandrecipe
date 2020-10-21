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

class Comment(models.Model):
    onpick = models.ForeignKey(OnpickYoutube, related_name='comments', on_delete=models.CASCADE,null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField('생성시간', auto_now_add=True,null=True)

   





