from django.shortcuts import render, HttpResponse

# graph testing


# Create your views here.


def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')    



# Need to add step 8 in authentication to the prfile create view