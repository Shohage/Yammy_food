# Generated by Django 3.1.7 on 2021-02-25 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210225_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resturantposition',
            name='rest_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='resturant_pos', serialize=False, to='main.resturantuser'),
        ),
    ]