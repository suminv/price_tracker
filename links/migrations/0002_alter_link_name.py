# Generated by Django 4.1.3 on 2022-11-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, max_length=220),
        ),
    ]