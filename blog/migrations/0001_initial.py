# Generated by Django 4.2.4 on 2023-08-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='main/', verbose_name='изображение')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='дата создания')),
                ('publication_attribute', models.BooleanField(default=True, verbose_name='публикация')),
                ('number_views', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
