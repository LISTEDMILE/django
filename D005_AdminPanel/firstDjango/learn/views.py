from django.shortcuts import render

# Create your views here.
def learn(request):
    return render(request,'learn/learnFile.html')

def learn2(request):
    return render(request,'learn/learnFile2.html')