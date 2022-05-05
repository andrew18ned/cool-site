from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404

from .forms import *
from .models import *


menu = [{'title' : 'Про сайт', 'url_name' : 'about'}, 
        {'title' : 'Добавити статтю', 'url_name' : 'add_page'}, 
        {'title' : 'Зворотній звязок', 'url_name' : 'contact'}, 
        {'title' : 'Увійти', 'url_name' : 'login'},] 

def index(request):
    posts = Women.objects.all()
    context = {
        'posts':posts, 
        'menu' : menu, 
        'title' : 'Головна',
        'cat_selected' : 0,
        }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', 
                    {'menu':menu, 'title':'Про сайт'})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForms(request.POST)
        if form.is_valid():
            # print(form.changed_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Помилка додавання статті')

    else:
        form = AddPostForms()
    return render(request, 'women/addpage.html', 
                {'form':form, 'menu':menu, 'title':'Додавання статті'})

def contact(request):
    return HttpResponse('Зворотній звязок')

def login(request):
    return HttpResponse('Авторизація')

def pageNotFound(request, exception):
    return HttpResponseNotFound('''<h1 style="color:darkblue">
    Сторінка не знайдена :(</h1><br>
    <a href="/">перейти на головну</a>''')

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post' : post,
        'menu' : menu,
        'title' : post.title,
        'cat_selected' : post.cat_id,
    }

    return render(request, 'women/post.html', context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
        
    context = {
        'posts':posts, 
        'menu' : menu, 
        'title' : 'Відображення по рубриках',
        'cat_selected' : cat_id,
        }
    return render(request, 'women/index.html', context=context)