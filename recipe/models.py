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