from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to home: ")

def about(request):
    return HttpResponse("About")