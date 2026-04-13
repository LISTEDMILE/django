from django.http import HttpResponse
from django.shortcuts import render

# render is used to render the file and send instead of sending text responses
# templates folder me hm apne html files rakh skte h aur static assets like css and js hm static folder me rakh skte h aur template hm kisko le rhe ye hme define karna padta h settings.py file of main project usme template nam ka object hota h
# templates kar app ke liye alag bhi le skte h aur poore project ka ek bhi rakh skte h
# folder structure me bhi rakh skte h templates ko par fir jab hm render karae to proper structure ke sath nam dena hota see route about
# static folder ko connect karne ke liye hme {% %} ka use karna hoga see home.html
# phele sbse uper likhenge { % load static %} jisse django ko pta chle static file load karni h
# fir jha pe stylesheet ko connect karne ke liye path dete h wha likhna h { % static  'file ka nam' %}
# but abhi bhi static file kha se uthani django ko nhi pata 
# to settings.py me jake STATICFILES_DIRS = path dena hoga
# uske liye hm os ko import karenge aur [os.path.join(BASE_DIR,'static)]   -- ab yha BASE_DIR is the main dir jo settings.py me hi dikh jaegi...

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'pages/about.html')