from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import *


menu = [{'title' : 'Про сайт', 'url_name' : 'about'}, 
        {'title' : 'Добавити статтю', 'url_name' : 'add_page'}, 
        {'title' : 'Зворотній звязок', 'url_name' : 'contact'}, 
        {'title' : 'Увійти', 'url_name' : 'login'},] 

def index(request):
    posts = Women.objects.all()
    context = {
        'posts':posts, 
        'menu':menu, 
        'title':'Головна',
        }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu':menu, 'title':'Про сайт'})

def addpage(request):
    return HttpResponse('Додавання статті')

def contact(request):
    return HttpResponse('Зворотній звязок')

def login(request):
    return HttpResponse('Авторизація')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 style="color:darkblue">Сторінка не знайдена :(</h1><br><a href="/">перейти на головну</a>')