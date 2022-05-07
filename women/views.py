from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


menu = [{'title' : 'Про сайт', 'url_name' : 'about'}, 
        {'title' : 'Добавити статтю', 'url_name' : 'add_page'}, 
        {'title' : 'Зворотній звязок', 'url_name' : 'contact'}, 
        {'title' : 'Увійти', 'url_name' : 'login'},] 



class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *,  object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Головна сторінка'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


# def index(request):
#     posts = Women.objects.all()
#     context = {
#         'posts':posts, 
#         'menu' : menu, 
#         'title' : 'Головна',
#         'cat_selected' : 0,
#         }
#     return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', 
                    {'menu':menu, 'title':'Про сайт'})



class AddPage(CreateView):
    form_class = AddPostForms
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *,  object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Додавання статті'
        context['menu'] = menu
        return context

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForms(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.changed_data)
#             form.save()
#             return redirect('home')

#     else:
#         form = AddPostForms()
#     return render(request, 'women/addpage.html', 
#                 {'form':form, 'menu':menu, 'title':'Додавання статті'})

def contact(request):
    return HttpResponse('Зворотній звязок')

def login(request):
    return HttpResponse('Авторизація')

def pageNotFound(request, exception):
    return HttpResponseNotFound('''<h1 style="color:darkblue">
    Сторінка не знайдена :(</h1><br>
    <a href="/">перейти на головну</a>''')




class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *,  object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'post' : post,
#         'menu' : menu,
#         'title' : post.title,
#         'cat_selected' : post.cat_id,
#     }

#     return render(request, 'women/post.html', context=context)



class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], 
                                        is_published=True)    

    def get_context_data(self, *,  object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категорія - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404()
        
#     context = {
#         'posts':posts, 
#         'menu' : menu, 
#         'title' : 'Відображення по рубриках',
#         'cat_selected' : cat_id,
#         }
#     return render(request, 'women/index.html', context=context)