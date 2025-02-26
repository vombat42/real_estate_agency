from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.migrations.operations.base import Operation
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import UniqueConstraint
from django.urls import reverse
from django.contrib.auth import get_user_model
from smart_selects.db_fields import ChainedForeignKey

# --------------------------------------------
# CATEGORY_CHOICES = (
#     (1, 'Жилая'),
#     (2, 'Коммерческая'),
# )
#
# TYPE_CHOICES = (
#     (1, 'Квартира'),
#     (2, 'Дом'),
#     (3, 'Участок'),
#     (11, 'Офисная'),
#     (12, 'Торговая'),
#     (13, 'Складская'),
#     (14, 'Производственная'),
#     (15, 'Прочая'),
# )

BATHROOM_CHOICES = (
    (1, 'Раздельный'),
    (2, 'Совмещенный'),
    (3, 'Общий'),
    (4, 'На улице'),
)

STATUS_CHOICES = (
    (1, 'Черновик'),
    (2, 'Опубликовано'),
    (3, 'Процесс сделки'),
    (4, 'Продано'),
    (5, 'Снято с публикации'),
)

OPERATION_CHOICES = (
    (1, 'Продажа'),
    (2, 'Аренда'),
)

class Estate(models.Model):
    """ объекты недвижимости """
    name = models.CharField(max_length=30, verbose_name='Заголовок')
    # category = models.IntegerField(choices=CATEGORY_CHOICES, null=True, verbose_name='Категория')
    # type = models.IntegerField(choices=TYPE_CHOICES, null=True, verbose_name='Тип')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='categories', verbose_name='Категория')
    type = ChainedForeignKey(
        'Type',  # Модель, с которой связано поле
        chained_field="category",  # Поле, от которого зависит выбор
        chained_model_field="category_id",  # Поле в модели Type, связанное с chained_field
        show_all=False,  # Показывать только связанные значения
        auto_choose=True,  # Автоматически выбирать значение, если оно единственное
        on_delete=models.PROTECT,
        related_name='types',
        verbose_name='Тип недвижимости'
    )
    operation = models.IntegerField(choices=OPERATION_CHOICES, verbose_name='Операция')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name='Статус объекта')
    description = models.TextField(verbose_name='Описание')
    floor = models.IntegerField(blank=True, default=None, null=True, verbose_name='Этаж')
    number_rooms = models.IntegerField(blank=True, default=None, null=True, verbose_name='Количество комнат')
    number_floors = models.IntegerField(blank=True, default=None, null=True, verbose_name='Этажность дома')
    total_area = models.FloatField(blank=True, default=None, null=True, verbose_name='Общая площадь')
    living_area = models.FloatField(blank=True, default=None, null=True, verbose_name='Жилая площадь')
    kitchen_area = models.FloatField(blank=True, default=None, null=True, verbose_name='Площадь кухни')
    bathroom = models.IntegerField(blank=True, choices=BATHROOM_CHOICES, null=True, verbose_name='Санузел')
    city = models.ForeignKey('City', on_delete=models.PROTECT, related_name='cities', verbose_name='Город')
    district = ChainedForeignKey(
        'District',  # Модель, с которой связано поле
        chained_field="city",  # Поле, от которого зависит выбор
        chained_model_field="city_id",  # Поле в модели District, связанное с chained_field
        show_all=False,  # Показывать только связанные значения
        auto_choose=True,  # Автоматически выбирать значение, если оно единственное
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='districts',
        verbose_name='Район'
    )
    street = models.CharField(blank=True, max_length=30, verbose_name='Улица')
    house = models.CharField(blank=True, max_length=10, verbose_name='Номер дома')
    apartment = models.CharField(blank=True, max_length=10, verbose_name='Номер квартиры')
    landmarks = models.CharField(blank=True, max_length=100, verbose_name='Ориентиры')
    owner_name = models.CharField(blank=True, max_length=30, verbose_name='Собственник (имя)')
    phone1 = PhoneNumberField(region='RU',blank=True, null=True, verbose_name='Телефон 1')
    # phone1 = models.CharField(blank=True, max_length=11, verbose_name='Телефон 1')
    phone2 = models.CharField(blank=True, max_length=11, verbose_name='Телефон 2')
    phone3 = models.CharField(blank=True, max_length=11, verbose_name='Телефон 3')
    telegram = models.CharField(blank=True, max_length=30, verbose_name='Телеграм')
    vk = models.CharField(blank=True, max_length=50, verbose_name='Страница ВК')
    creator = models.ForeignKey(get_user_model(), blank=True, null=True, on_delete=models.SET_NULL, related_name='creators', verbose_name='Создал запись')
    modifier = models.ForeignKey(get_user_model(), blank=True, null=True, on_delete=models.SET_NULL, related_name='modifiers', verbose_name='Изменил запись')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объект недвижимости"
        verbose_name_plural = "Объекты недвижимости"
        ordering = ['time_create']
        # indexes = [models.Index(fields=['time_create'])]

    # def save(self, *args, **kwargs):
    #     if not self.creator_id:  # Если поле user не заполнено
    #         self.creator = get_current_user()  # Заполняем текущим пользователем
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('realtor:estate', kwargs={'estate_slug': self.slug})


class Category(models.Model):
    """ справочник категорий недвижимости """
    name = models.CharField(unique=True, max_length=20, verbose_name='Категрия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категрия недвижимости"
        verbose_name_plural = "Категрии недвижимости"


class Type(models.Model):
    """ справочник типов недвижимости """
    name = models.CharField(max_length=30, verbose_name='Тип')
    category_id = models.ForeignKey('Category', null=True, on_delete=models.CASCADE, related_name='categories_id', verbose_name='Категрия')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип недвижимости"
        verbose_name_plural = "Типы недвижимости"
        constraints = [
            UniqueConstraint(
                fields=['name', 'category_id'],  # Уникальное сочетание name и category_id
                name='unique_name_category'  # Имя ограничения
            )
        ]


class City(models.Model):
    """ справочник городов """
    name = models.CharField(unique=True, max_length=20, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class District(models.Model):
    """ справочник районов городов """
    name = models.CharField(max_length=30, verbose_name='Район')
    city_id = models.ForeignKey('City', null=True, on_delete=models.CASCADE, related_name='cities_id', verbose_name='Город')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"
        constraints = [
            UniqueConstraint(
                fields=['name', 'city_id'],  # Уникальное сочетание name и city_id
                name='unique_name_city'  # Имя ограничения
            )
        ]


class EstateImage(models.Model):
    """ Изображения """
    estate = models.ForeignKey('Estate', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/estates/')

    def __str__(self):
        return f"Image for {self.estate.name}"

    class Meta:
        verbose_name = "Фото объекта"
        verbose_name_plural = "Фото объекта"