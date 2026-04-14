from django.http import HttpResponse
from django.shortcuts import render

# ap admin panel create karne se pehle python manage.py migrate
# fir  python manage.py createsuperuser
# fir usme nam email not required and pass...

# username - this
# this time the pass is 123

#

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'pages/about.html')