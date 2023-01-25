from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound, Http404
from django.views.generic import ListView

from .models import *
from .forms import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add article", 'url_name': 'add_page'},
        {'title': "Contacts", 'url_name': 'contact'},
        {'title': "Log in", 'url_name': 'login'}
        ]


class ScheduleHome(ListView):
    model = Rocket
    template_name = 'schedule/index.html'


# def index(request):
#     posts = Rocket.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Main page',
#         'type_selected': 0,
#     }
#     return render(request, 'schedule/index.html', context=context)


def about(request):
    return render(request, 'schedule/about.html', {'menu': menu, 'title': 'About'})


def rockets(request):
    return render(request, 'schedule/index.html', {'menu': menu, 'title': 'Rockets'})


def contacts(request):
    return render(request, 'schedule/contacts.html', {'menu': menu, 'title': 'Contacts'})


def login(request):
    return render(request, 'schedule/about.html', {'menu': menu, 'title': 'Log in'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, "schedule/addpage.html", {'form': form, 'title': 'Add rocket'})


def show_post(request, post_slug):
    from schedule.models import Rocket
    post = get_object_or_404(Rocket, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'type_selected': post.type_id,
    }

    return render(request, 'schedule/post.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Page not found :( </h1>')


def show_type(request, type_slug):
    type = Type.objects.filter(slug=type_slug)
    posts = Rocket.objects.filter(type_id=type[0].id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Showing by category',
        'type_selected': type[0].id,
    }
    return render(request, 'schedule/index.html', context=context)
