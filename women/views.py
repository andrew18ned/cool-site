from nis import cat
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render



def index(request):
    return HttpResponse('<h1>Сторінка програми women</h1><br><a href="/cats/1/">category</a><br><a href="/archive/0000/">arhive</a><br><a href="/eee">перейти на незнайдену сторінку</a>')


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