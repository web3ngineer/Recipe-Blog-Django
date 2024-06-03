from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/auth/signin')
def userReceipe(request,username):
    user = User.objects.get(username=username)
    # print(user.id)
    queryset = Receipe.objects.filter(user=user.id)
    context = {'receipes': queryset}

    if request.GET.get("search"):
        search = request.GET.get("search")
        queryset = queryset.filter(receipe_name__icontains = search)
        context = {'receipes': queryset, 'search':True}

    return render(request, 'user_receipe.html', context)


@login_required(login_url='/auth/signin')
def addReceipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')

        # print(receipe_desc, receipe_name, receipe_image)
        user = User.objects.get(username=request.user)
        Receipe.objects.create(
            user_id= user.id,
            receipe_name = receipe_name,
            receipe_desc = receipe_desc,
            receipe_image = receipe_image
        )
        return redirect(f'/receipe/user/{request.user}')

    return render(request, 'add_receipe.html')


@login_required(login_url='/auth/signin')
def deleteReceipe(request,id):
    print(id)
    Receipe.objects.filter(id=id).delete()
    return redirect(f'/receipe/user/{request.user}')


@login_required(login_url='/auth/signin')
def updateReceipe(request,id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')

        queryset.receipe_name = receipe_name
        queryset.receipe_desc = receipe_desc

        if receipe_image:
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect(f'/receipe/user/{request.user}')
    
    context = {'receipe': queryset}
    # print(queryset.receipe_name)
    return render(request, 'update_receipe.html', context)
