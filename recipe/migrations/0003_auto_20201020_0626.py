# Generated by Django 3.1.2 on 2020-10-19 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20201020_0622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diet',
            old_name='diet_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='food_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='life',
            old_name='life_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='style',
            old_name='style_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='diet',
            name='ip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip'),
        ),
        migrations.AlterField(
            model_name='food',
            name='ip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip'),
        ),
        migrations.AlterField(
            model_name='life',
            name='ip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='ip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip'),
        ),
        migrations.AlterField(
            model_name='style',
            name='ip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ip'),
        ),
    ]
