# Generated by Django 3.1.2 on 2020-10-21 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20201021_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trendcomment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trendcomment',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.trend'),
        ),
    ]