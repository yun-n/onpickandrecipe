# Generated by Django 3.1.2 on 2020-10-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onpick', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnpickYoutube',
            fields=[
                ('onpick_id', models.AutoField(primary_key=True, serialize=False)),
                ('onpick_title', models.CharField(blank=True, max_length=200, null=True)),
                ('onpick_content', models.CharField(blank=True, max_length=3000, null=True)),
            ],
        ),
    ]