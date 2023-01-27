from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *



# class ScheduleHome(ListView):
#     model = Rocket
#     template_name = 'schedule/index.html'


class ScheduleHome(DataMixin, ListView):
    model = Rocket
    template_name = 'schedule/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Rocket.objects.filter(is_published=True).select_related('type')



def about(request):
    return render(request, 'schedule/about.html', {'title': 'About'})


def rockets(request):
    return render(request, 'schedule/index.html', {'title': 'Rockets'})


def contacts(request):
    return render(request, 'schedule/contacts.html', {'title': 'Contacts'})


def login(request):
    return render(request, 'schedule/about.html', {'title': 'Log in'})


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


def show_type(request, type_slug):
    type = Type.objects.filter(slug=type_slug)
    posts = Rocket.objects.filter(type_id=type[0].id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Showing by types',
        'type_selected': type[0].id,
    }
    return render(request, 'schedule/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Page not found :( </h1>')
