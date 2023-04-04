from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
import datetime
import requests
from django.shortcuts import render


from .forms import AddPostForm, RegisterUserForm, LoginUserForm, LatinToCyrillicForm
from .utils import DataMixin, latin_to_cyrillic
from .models import Launcher, Rocket


class ScheduleHome(DataMixin, ListView):
    # Define the Rocket model as the data source for the view
    model = Rocket

    # Set the name of the template to be used to render the view
    template_name = 'schedule/index.html'

    # Set the name of the context variable that will contain the list of rockets
    context_object_name = 'posts'

    # Override the get_context_data method to add additional context variables
    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the parent class's get_context_data method to get the default context data
        context = super().get_context_data(**kwargs)

        # Call the DataMixin class's get_user_context method to get user-specific context data
        c_def = self.get_user_context(title="Main page")

        # Merge the default and user-specific context data into a single dictionary
        return dict(list(context.items()) + list(c_def.items()))

    # Override the get_queryset method to filter the list of rockets by is_published status
    def get_queryset(self):
        return Rocket.objects.filter(is_published=True).select_related('type')


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
    l_rockets = Rocket.objects.select_related('location')

    context = {
        'l_rockets': l_rockets,
        'location': location,
        'title': location.name,
    }

    return render(request, 'schedule/location.html', context=context)


def show_agency(request, slug):
    # Import the Agency model and get_object_or_404 function
    from schedule.models import Agency
    from django.shortcuts import get_object_or_404

    # Use get_object_or_404 to retrieve an Agency instance based on the slug
    agency = get_object_or_404(Agency, slug=slug)

    # Define a context dictionary with data to be passed to the template
    context = {
        'agency': agency,
        'title': agency.name,
    }

    # Render the agency.html template with the context data
    return render(request, 'schedule/agency.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Page not found :( </h1>')


def next_launch(request):
    url = 'https://ll.thespacedevs.com/2.2.0/launch/upcoming/'
    params = {'mode': 'detailed', 'limit': 10, 'offset': 0}

    response = requests.get(url, params=params)

    launches = response.json()['results']

    # Calculate the difference between the current date and the next launch date
    now = datetime.datetime.now(datetime.timezone.utc)
    next_launch_date_str = launches[0]['net']
    next_launch_date = datetime.datetime.fromisoformat(next_launch_date_str[:-1]).replace(tzinfo=datetime.timezone.utc)
    difference = next_launch_date - now
    difference_str = f"{difference.days} days, {difference.seconds // 3600} hours, {(difference.seconds // 60) % 60} minutes"

    context = {
        'launches': launches,
        'difference': difference_str
    }
    return render(request, 'schedule/next_launch.html', context)


def update_database():
    url = 'https://ll.thespacedevs.com/2.2.0/config/launcher/'
    response = requests.get(url)
    data = response.json()
    
    for item in data['results']:
        launcher, created = Launcher.objects.get_or_create(
            id=item['id'],
            defaults={
                'title': item['name'], 
                # 'description': item['manufacturer'], 
                'family': item['family'],
                'full_name': item['full_name']
            }
        )
        
        # update the launcher's fields
        launcher.title = item['name']
        # launcher.title = item['description']
        launcher.family = item['family']
        launcher.full_name = item['variant']
        
        # save the changes to the database
        launcher.save()


def launcher_list(request):
    # update the database with the latest information
    update_database()

    # retrieve a list of all launchers from the database
    launchers = Launcher.objects.all()

    # render the list of launchers in an HTML template
    context = {'launchers': launchers}
    return render(request, 'schedule/launcher.html', context)


def convertor(request):
    form = LatinToCyrillicForm()
    translated_text = ''
    if request.method == 'POST':
        form = LatinToCyrillicForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('my_text_input')
            language = form.cleaned_data.get('my_language_choice')
            # Split text into lines and translate each line separately
            translated_lines = []
            for line in text.split('\n'):
                translated_lines.append(latin_to_cyrillic(line.strip(), language))
            # Join translated lines back into a single string with line breaks
            translated_text = '\n'.join(translated_lines)
    context = {'form': form, 'translated_text': translated_text}
    return render(request, 'schedule/convert_text.html', context)



