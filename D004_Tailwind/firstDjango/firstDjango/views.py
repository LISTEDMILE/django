from django.http import HttpResponse
from django.shortcuts import render

# tailwind use karne ke liye pehle 
# pip install django-tailwind
# pip install 'django-tailwind[reload]' this is for ki bar bar auto update hoti rhe....
# fir hm main settings.py me jake ek app add karenge tailwind name se
# uske bad python manage.py tailwind init
# fir app nam mangega default theme hota h whi rehne do..
# fir jo theme nam h jaise uska forder create hoga us nam ko app me bhi add karo settings.py me
# fir settings.py me hi likho TAILWIND_APP_NAME = 'theme'
# INTERNAL_IPS = ['127.0.0.1']
# ab hmari tailwind as a folder aa chuki h to
# simply python manage.py tailwind install  isse hmari tailwind install ho jaegiii....
# ab jo theme me base.html file hogi usme 2 cheeze same apni un files me add karni jha hm tailwind chahte h.
# {% load static tailwind_tags %}
# {% tailwind_css %}
# ab pehle hme ek doosre terminal pe python manage.py tailwind start
# aur fir apna server start karenge....
# also pehle kisi terminal se pta karo where npm likhke ki kha h npm
# wo path dalo settings.py me NPM_BIN_PATH = r"path"  ,,, r taki \ dikkat na de....
# ab chal to gya but bar bar reload na karna pade iske liye app add karenge settings.py me 'django_browser_relaod'
# add karenge settings.py me middleware    --  'django_browser_reload.middleware.BrowserReloadMiddleware',  --- make sure isko sabse last me hi rakhe....
# fir jo hmari main app wali urls file file h usme ek route add karenge  ---   path("__reload__/",include("django_browser_reload.urls")),   ---- make sure ye bhi last me hi ho...
# and done ab hm use karskte h tailwind

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'pages/about.html')