import boto3
import uuid
import requests
from bs4 import BeautifulSoup
from .models import Profile, Photo, Activity
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# login imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# photo import

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com'
BUCKET = 'miloprofilepics'

# Create your views here.


def home(request):
    toReturn = webscrapper()
    return render(request, 'home.html',
                  {
                      'toReturn': toReturn
                  })


def profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    activity = Activity.objects.filter(user_id=request.user.id)
    return render(request, 'profile.html',
                  {
                      'profile': profile,
                      'activity': activity
                  }
                  )


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('../profile/create')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def webscrapper():
    url = "https://www.ideafit.com/fitness-library"
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    grabbedfeed = content.find_all("div", attrs={
                                   "class": "box white article teaser large wide nopad has-image clearfix"})
    toReturn = []
    for x in range(6):
        artical = {
            'img': grabbedfeed[x].img.get("src"),
            'link': url + grabbedfeed[x].h3.a.get('href'),
            'headline': grabbedfeed[x].h3.text,
            'discript': grabbedfeed[x].p.text
        }
        toReturn.append(artical)
    return toReturn


class ProfileCreate(CreateView):
    model = Profile
    fields = ['name', 'dob', 'sport_bio', 'goal']
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['name', 'sport_bio', 'goal']
    sucess_url = '/profile/'


class ActivityCreate(CreateView):
    model = Activity
    fields = ['activity', 'weight', 'reps', 'date']
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ActivityDelete(DeleteView):
    model = Activity
    fields = ['activity', 'weight', 'reps', 'date']
    success_url = '/profile/'


def add_photo(request, profile_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, profile_id=profile_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('/profile/')
