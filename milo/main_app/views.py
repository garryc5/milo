from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
#login imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile

from bs4 import BeautifulSoup
import requests


# Create your views here.

def home(request):
    toReturn = webscrapper()
    return render(request, 'home.html',
    {
      'toReturn': toReturn
    })

def profile(request):
    profile=Profile.objects.get(user_id = request.user.id)
    return render(request, 'profile.html',
    {
      'profile' : profile,
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
  response = requests.get(url , timeout=5)
  content = BeautifulSoup(response.content, "html.parser")
  grabbedfeed = content.find_all("div", attrs={"class": "box white article teaser large wide nopad has-image clearfix"})
  toReturn = []
  for x in range(6):
    artical = {
        'img' : grabbedfeed[x].img.get("src"),
        'link' : url + grabbedfeed[x].h3.a.get('href'),
        'headline' : grabbedfeed[x].h3.text,
        'discript' : grabbedfeed[x].p.text
    }
    toReturn.append(artical)
  return toReturn

class ProfileCreate(CreateView):
  model = Profile
  fields = ['name','dob','picture','sport_bio','goal']
  success_url='/profile/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ProfileUpdate(UpdateView):
  model = Profile
  fields= ['name','picture','sport_bio','goal']
  sucess_url = '/profile/'