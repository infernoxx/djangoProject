# Generated by Django 4.1.3 on 2022-11-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('rating_nums', models.CharField(max_length=100)),
                ('rating_people', models.CharField(max_length=100)),
                ('press', models.CharField(max_length=100)),
                ('publication_time', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('book_img', models.CharField(max_length=100)),
                ('book_summary', models.CharField(max_length=100)),
                ('book_target', models.CharField(max_length=50)),
            ],
        ),
    ]