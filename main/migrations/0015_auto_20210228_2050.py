# Generated by Django 3.1.7 on 2021-02-28 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_resturantuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturantuser',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rest_place', to='main.place'),
        ),
        migrations.DeleteModel(
            name='ResturantPosition',
        ),
    ]
