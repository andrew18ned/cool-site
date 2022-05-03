from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import *


menu = ['Про сайт', 'Добавити статтю', 'Зворотній зв*язок', 'Увійти']

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts':posts, 'menu':menu, 'title':'Головна'})


def about(request):
    return render(request, 'women/about.html', {'menu':menu, 'title':'Про сайт'})


def category(request, catid):
    if request.GET:
        print(request.GET)
    if catid == 10:
        return redirect('home', permanent=True)
    catid += 1

    return HttpResponse(f'<h1>Сторінка категорій</h1><p>{catid}</p><br><a href="/cats/{catid}/">перейти на наступну сторінку</a><br><a href="/">перейти на головну</a>')


def archive(request, year):
    return HttpResponse(f'<center><h1 style="color:red">Сторінка містить архів по роках</h1><p>{year}</p><br><a href="/">перейти на головну</a></center>')



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 style="color:darkblue">Сторінка не знайдена :(</h1><br><a href="/">перейти на головну</a>')