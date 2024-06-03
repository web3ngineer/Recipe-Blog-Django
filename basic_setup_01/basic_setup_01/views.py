from django.shortcuts import render
from django.http import HttpResponse
from recipeProject.models import *

def main(request):
    # return HttpResponse("Hello You are at main page")
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}

    if request.GET.get("search"):
        search = request.GET.get("search")
        queryset = queryset.filter(receipe_name__icontains = search)
        context = {'receipes': queryset, 'search':True}

    return render(request, 'main.html', context)

def layout(request):
    return render(request, 'layout.html')