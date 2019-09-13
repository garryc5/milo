from django.shortcuts import render, HttpResponse

# graph testing


# Create your views here.


def home(request):
    return render(request, 'home.html')
