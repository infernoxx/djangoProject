# Generated by Django 4.1.3 on 2022-11-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_book_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_info',
            name='book_summary',
            field=models.CharField(max_length=300),
        ),
    ]