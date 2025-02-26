# Generated by Django 5.1 on 2025-02-21 14:10

import django.db.models.deletion
import smart_selects.db_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Категрия')),
            ],
            options={
                'verbose_name': 'Категрия недвижимости',
                'verbose_name_plural': 'Категрии недвижимости',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Район')),
                ('city_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities_id', to='realtor.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование')),
                ('operation', models.IntegerField(choices=[(1, 'Продажа'), (2, 'Аренда')], verbose_name='Операция')),
                ('status', models.IntegerField(choices=[(1, 'Черновик'), (2, 'Опубликовано'), (3, 'Процесс сделки'), (4, 'Продано'), (5, 'Снято с публикации')], default=1, verbose_name='Статус объекта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('floor', models.IntegerField(blank=True, default=None, null=True, verbose_name='Этаж')),
                ('number_rooms', models.IntegerField(blank=True, default=None, null=True, verbose_name='Количество комнат')),
                ('number_floors', models.IntegerField(blank=True, default=None, null=True, verbose_name='Этажность дома')),
                ('total_area', models.FloatField(blank=True, default=None, null=True, verbose_name='Общая площадь')),
                ('living_area', models.FloatField(blank=True, default=None, null=True, verbose_name='Жилая площадь')),
                ('kitchen_area', models.FloatField(blank=True, default=None, null=True, verbose_name='Площадь кухни')),
                ('bathroom', models.IntegerField(blank=True, choices=[(1, 'Раздельный'), (2, 'Совмещенный'), (3, 'Общий'), (4, 'На улице')], null=True, verbose_name='Санузел')),
                ('street', models.CharField(blank=True, max_length=30, verbose_name='Улица')),
                ('house', models.CharField(blank=True, max_length=10, verbose_name='Номер дома')),
                ('apartment', models.CharField(blank=True, max_length=10, verbose_name='Номер квартиры')),
                ('landmarks', models.CharField(blank=True, max_length=100, verbose_name='Ориентиры')),
                ('owner_name', models.CharField(blank=True, max_length=30, verbose_name='Собственник')),
                ('phone1', models.CharField(blank=True, max_length=11, verbose_name='Телефон 1')),
                ('phone2', models.CharField(blank=True, max_length=11, verbose_name='Телефон 2')),
                ('phone3', models.CharField(blank=True, max_length=11, verbose_name='Телефон 3')),
                ('telegram', models.CharField(blank=True, max_length=30, verbose_name='Телеграм')),
                ('vk', models.CharField(blank=True, max_length=50, verbose_name='Страница ВК')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='realtor.category', verbose_name='Категория')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='realtor.city', verbose_name='Город')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creators', to=settings.AUTH_USER_MODEL, verbose_name='Создал запись')),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='city', chained_model_field='city_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='districts', to='realtor.district', verbose_name='Район')),
                ('modifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Изменил запись')),
            ],
            options={
                'verbose_name': 'Объект недвижимости',
                'verbose_name_plural': 'Объекты недвижимости',
                'ordering': ['time_create'],
            },
        ),
        migrations.CreateModel(
            name='EstateImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/estates/')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='realtor.estate')),
            ],
            options={
                'verbose_name': 'Фото объекта',
                'verbose_name_plural': 'Фото объекта',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тип')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories_id', to='realtor.category', verbose_name='Категрия')),
            ],
            options={
                'verbose_name': 'Тип недвижимости',
                'verbose_name_plural': 'Типы недвижимости',
            },
        ),
        migrations.AddField(
            model_name='estate',
            name='type',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category_id', on_delete=django.db.models.deletion.PROTECT, related_name='types', to='realtor.type', verbose_name='Тип недвижимости'),
        ),
        migrations.AddConstraint(
            model_name='district',
            constraint=models.UniqueConstraint(fields=('name', 'city_id'), name='unique_name_city'),
        ),
        migrations.AddConstraint(
            model_name='type',
            constraint=models.UniqueConstraint(fields=('name', 'category_id'), name='unique_name_category'),
        ),
    ]
