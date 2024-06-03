from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello You are at home page")
    return render(request, 'home/home.html')

def home1(request):
    # return HttpResponse("Hello Your are at Home1 page")
    return render(request, 'home1.html')

def about(request):
    context = {'title':'About'}
    return render(request, 'home/about.html', context)

def contact(request):
    return render(request, 'home/contact.html')

