# Generated by Django 4.1.1 on 2022-09-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_item_date_to_do'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_to_do',
            field=models.DateField(null=True, verbose_name='Дата выполнения'),
        ),
    ]
