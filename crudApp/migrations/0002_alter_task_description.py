# Generated by Django 5.0.2 on 2024-02-28 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(),
        ),
    ]