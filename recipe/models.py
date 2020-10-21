from django.db import models

class ip(models.Model):
    ip_id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=45, unique=True)

class Trend(models.Model):
    id = models.AutoField(primary_key=True)
    trend_title = models.CharField(max_length=45, null=True)
    trend_content = models.CharField(max_length=500, null=True)
    trend_video = models.FileField()
    ip = models.ForeignKey('ip', on_delete=models.CASCADE, null=True)

class Food(models.Model):
    id = models.AutoField(primary_key=True)
    food_title = models.CharField(max_length=45, null=True)
    food_content = models.CharField(max_length=500, null=True)
    food_video = models.FileField()
    ip = models.ForeignKey('ip', on_delete=models.CASCADE, null=True)

class Style(models.Model):
    id = models.AutoField(primary_key=True)
    style_title = models.CharField(max_length=45, null=True)
    style_content = models.CharField(max_length=500, null=True)
    style_video = models.FileField()
    ip = models.ForeignKey('ip', on_delete=models.CASCADE, null=True)

class Diet(models.Model):
    id = models.AutoField(primary_key=True)
    diet_title = models.CharField(max_length=45, null=True)
    diet_content = models.CharField(max_length=500, null=True)
    diet_video = models.FileField()
    ip = models.ForeignKey('ip', on_delete=models.CASCADE, null=True)

class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    pet_title = models.CharField(max_length=45, null=True)
    pet_content = models.CharField(max_length=500, null=True)
    pet_video = models.FileField()
    ip = models.ForeignKey('ip', on_delete=models.CASCADE, null=True)

class Life(models.Model):
    id = models.AutoField(primary_key=True)
    life_title = models.CharField(max_length=45, null=True)
    life_content = models.CharField(max_length=500, null=True)
    life_video = models.FileField()
    ip = models.ForeignKey('ip', on_delete=models.CASCADE, null=True)

#<------------------------------------------->

class TrendComment(models.Model):
    recipe = models.ForeignKey('Trend', related_name='comments', on_delete=models.CASCADE,null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    comment = models.CharField(max_length=100,null=True)
    

class FoodComment(models.Model):
    recipe = models.ForeignKey(Food, related_name='comments', on_delete=models.CASCADE,null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField('생성시간', auto_now_add=True,null=True)

class StyleComment(models.Model):
    recipe = models.ForeignKey(Style, related_name='comments', on_delete=models.CASCADE,null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField('생성시간', auto_now_add=True,null=True)

class DietComment(models.Model):
    recipe = models.ForeignKey(Diet, related_name='comments', on_delete=models.CASCADE,null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField('생성시간', auto_now_add=True,null=True)

class PetComment(models.Model):
    recipe = models.ForeignKey(Pet, related_name='comments', on_delete=models.CASCADE,null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField('생성시간', auto_now_add=True,null=True) 

class LifeComment(models.Model):
    recipe = models.ForeignKey(Life, related_name='comments', on_delete=models.CASCADE,null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField('생성시간', auto_now_add=True,null=True)   