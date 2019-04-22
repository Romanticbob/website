from django.shortcuts import render
from django.http import HttpResponse
from .form import *

# Create your views here.


def index(request):
    if request.method == 'GET':
        product = ProductForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductForm(request.POST)
        if product.is_valid():
            # 获取网页控件name的数据
            # 方法一
            name = product['name']
            # 方法二
            # cleaned_data将控件name数据进行清洗,转换成python数据类型
            cname = product.cleaned_data['name']
            return HttpResponse('提交成功')
        else:
            # 将错误信息输出，error_msg是将错误信息以json格式输出
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())
