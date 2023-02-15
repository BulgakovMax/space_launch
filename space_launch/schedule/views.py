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


class ScheduleHome(DataMixin, ListView):
    model = Rocket
    template_name = 'schedule/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Rocket.objects.filter(is_published=True).select_related('type')


def about(request):
    return render(request, 'schedule/about.html', {'title': 'About'})


def rockets(request):
    return render(request, 'schedule/rockets.html', {'title': 'rockets'})


def locations(request):
    from schedule.models import Location
    locations = Location.objects.order_by('name').values()

    return render(request, 'schedule/locations.html', {'title': 'Locations', 'locations': locations})


def agencies(request):
    from schedule.models import Agency
    agencies = Agency.objects.order_by('name').values()

    return render(request, 'schedule/agencies.html', {'title': 'Agencies', 'agencies': agencies})


def contacts(request):
    return render(request, 'schedule/contacts.html', {'title': 'Contacts'})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'schedule/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'schedule/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorization")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


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


def show_location(request, slug):
    from schedule.models import Location
    location = get_object_or_404(Location, slug=slug)

    context = {
        'location': location,
        'title': location.name,
    }

    return render(request, 'schedule/location.html', context=context)


def show_agency(request, slug):
    from schedule.models import Agency
    agency = get_object_or_404(Agency, slug=slug)

    context = {
        'agency': agency,
        'title': agency.name,
    }

    return render(request, 'schedule/agency.html', context=context)


# class ShowLocation(DataMixin, ListView):
#     model = Location
#     template_name = 'schedule/location.html'
#     context_object_name = 'location'
#     # allow_empty = False
#
#     def get_queryset(self):
#         return Location.objects.filter(name=self.kwargs['location_slug']).select_related('name')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c = Location.objects.get(slug=self.kwargs['location_slug'])
#         c_def = self.get_user_context(title='Location' + str(c.name),
#                                       type_selected=c.pk)
#         return dict(list(context.items()) + list(c_def.items()))


class RocketType(DataMixin, ListView):
    model = Rocket
    template_name = 'schedule/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Rocket.objects.filter(type__slug=self.kwargs['type_slug'], is_published=True).select_related('type')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Type.objects.get(slug=self.kwargs['type_slug'])
        c_def = self.get_user_context(title='Types of rockets - ' + str(c.name),
                                      type_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


# def show_type(request, type_slug):
#     type = Type.objects.filter(slug=type_slug)
#     posts = Rocket.objects.filter(type_id=type[0].id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'title': 'Showing by types',
#         'type_selected': type[0].id,
#     }
#     return render(request, 'schedule/index.html', context=context)
#
#
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Page not found :( </h1>')
