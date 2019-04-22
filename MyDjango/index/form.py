from django import forms
from .models import *
from django.core.exceptions import  ValidationError


def weight_validate(value):
    if not str(value).isdigit():
        raise ValidationError('请输入正确的重量')


class ProductForm(forms.Form):
    name = forms.CharField(max_length=20, label='名字', widget=forms.widgets.TextInput(attrs={'class': 'c1'}),
                           error_messages={'required': '名字不可为空'},)
    weight = forms.CharField(max_length=50, label='重量', validators=[weight_validate])
    size = forms.CharField(max_length=50, label='尺寸')
    choices_list = [(i + 1, v['type_name']) for i, v in enumerate(Type.objects.values('type_name'))]
    type = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class': 'c1', 'size': '4'}), choices=choices_list,
                             label='产品类型')
