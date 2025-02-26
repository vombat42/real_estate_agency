from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from multiupload.fields import MultiFileField
from phonenumber_field.formfields import PhoneNumberField

from .models import Estate, EstateImage


# @deconstructible
# class RussianValidator:
#     ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
#     code = 'russian'
#
#     def __init__(self, message=None):
#         self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел."
#
#     def __call__(self, value, *args, **kwargs):
#         if not (set(value) <= set(self.ALLOWED_CHARS)):
#             raise ValidationError(self.message, code=self.code)


class EstateCreateForm(forms.ModelForm):
    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024 * 1024 * 5)  # До 10 файлов, каждый до 5 МБ

    class Meta:
        model = Estate
        phone1 = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('Phone')}), required=False)
        widgets = {
            'phone2': forms.TextInput(attrs={"class": "form-phone-input",
                                             'type': 'tel',
                                             'placeholder':"X (XXX) XXX-XX-XX",
                                             'pattern':"[0-9]\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}",
                                             'autocomplete': "tel"}),
            'phone3': forms.TextInput(attrs={"class": "form-phone-input",
                                             'type': 'tel',
                                             'placeholder': "X (XXX) XXX-XX-XX",
                                             'pattern': "[0-9]\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}",
                                             'autocomplete': "tel"}),
        }
        fields = '__all__'

        # < input
        # type = "tel"
        # id = "phone"
        # name = "phone"
        # placeholder = "+7 (XXX) XXX-XX-XX"
        # autocomplete = "tel"
        # required >
        # fields = [
        #     'name',
        #     'category',
        #     'type',
        #     'operation',
        #     'status',
        #     'description',
        #     'floor',
        #     'number_rooms',
        #     'number_floors',
        #     'total_area',
        #     'living_area',
        #     'kitchen_area',
        #     'bathroom',
        #     'city',
        #     'district',
        #     'street',
        #     'house',
        #     'apartment',
        #     'landmarks',
        #     'owner_name',
        #     'phone1',
        #     'phone2',
        #     'phone3',
        #     'telegram',
        #     'vk',
        #     'slug',
        #     'images',
        # ]
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-input'}),
        #     'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        # }
        # labels = {'slug': 'URL'}

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 50:
    #         raise ValidationError("Длина превышает 50 символов")
    #
    #     return title


# class UploadFileForm(forms.Form):
#     file = forms.ImageField(label="Файл")