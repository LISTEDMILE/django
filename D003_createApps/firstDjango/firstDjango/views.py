from django.http import HttpResponse
from django.shortcuts import render

# ab agar hm koi bhi app create ya bahar se import karenge pehle to app create karne ke liye manage.py startapp app ka nam aur fir settings.py me resgister karenge app
# ab agar hme same template use karni global to thik nhi to alag se app ki template bhi bna skte h
# ab hmare project me to url h but app ke andar kaise route kare
# uske liye hmne urls.py bnai app me uske liye poori project global wali file copy paste karke edit kardi
# per the q is ki jo access h flow h outer urls.py ke pas wo hmare app wale urls.py ke pas kaise aaega
# ab jo global wala urls.py h usme apne app ka route dalenge aur jaise views ka koi function execute karate the is bar dalenge includes('app ka nam.urls') ab isse kya hoga django app ka nam jo dala us nam ka app dhoondega aur use urls ko control dedega see urls.py
# ab hm na ek layout type ka bhi bna skte h jisme hm layout design karde aur kuch var use karde ab jab bhi koi nya page dena ho bas wo var ke nam send kardo
# {% block name of var %} Defautl val {%endblock%}
# jis jis file me use karna h just likho {%extends "layout file ka nam"%}
# aur var provide karne ke liye {% block name of var %} val {%endblock%}
# see extends me pehle check karega layout wali file same app me nhi mili to usse uper jaise yha seedha root global program wale template me


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'pages/about.html')