# Generated by Django 3.1.2 on 2020-10-19 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ip',
            fields=[
                ('ip_id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('trend_id', models.AutoField(primary_key=True, serialize=False)),
                ('trend_title', models.CharField(max_length=45, null=True)),
                ('trend_content', models.CharField(max_length=500, null=True)),
                ('trend_video', models.FileField(upload_to='')),
                ('ip', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('style_id', models.AutoField(primary_key=True, serialize=False)),
                ('style_title', models.CharField(max_length=45, null=True)),
                ('style_content', models.CharField(max_length=500, null=True)),
                ('style_video', models.FileField(upload_to='')),
                ('ip', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('pet_id', models.AutoField(primary_key=True, serialize=False)),
                ('pet_title', models.CharField(max_length=45, null=True)),
                ('pet_content', models.CharField(max_length=500, null=True)),
                ('pet_video', models.FileField(upload_to='')),
                ('ip', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip')),
            ],
        ),
        migrations.CreateModel(
            name='Life',
            fields=[
                ('life_id', models.AutoField(primary_key=True, serialize=False)),
                ('life_title', models.CharField(max_length=45, null=True)),
                ('life_content', models.CharField(max_length=500, null=True)),
                ('life_video', models.FileField(upload_to='')),
                ('ip', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_title', models.CharField(max_length=45, null=True)),
                ('food_content', models.CharField(max_length=500, null=True)),
                ('food_video', models.FileField(upload_to='')),
                ('ip', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip')),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('diet_id', models.AutoField(primary_key=True, serialize=False)),
                ('diet_title', models.CharField(max_length=45, null=True)),
                ('diet_content', models.CharField(max_length=500, null=True)),
                ('diet_video', models.FileField(upload_to='')),
                ('ip', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip')),
            ],
        ),
    ]
