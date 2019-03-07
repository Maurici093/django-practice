from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render, 
    get_object_or_404,
    redirect
)
from django.template import loader
from .models import Destination
from .forms import DestinationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import (
    authenticate, 
    login, 
    logout
)
from django.contrib.auth.models import User

# Create your views here.

'''def show_destination(request):
    destination = Destination.objects.order_by('id')
    template = loader.get_template('index.html')
    page_title = 'Ecoturismo En Colombia - Native Colombia - Agencia especializada'
    banner_description = 'Vive Experiencias Naturales'
    context = {
        'destination': destination,
        'page_title': page_title,
        'banner_description': banner_description,
    }
    return HttpResponse(template.render(context,request))'''

'''def saludo(request):
    template = loader.get_template('saludo.html')
    big_title = 'Este es el titulo del header'
    title = 'Vive una Experiencia Natural'
    context = {
        'big_title': big_title,
        'title': title
    }
    return HttpResponse(template.render(context, request))'''

'''def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    template = loader.get_template('destination_detail.html')
    title = 'Descripción - Destino:'
    context = {
        'destination': destination,
        'title': title
    }
    return HttpResponse(template.render(context,request))'''

@login_required()
def new_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save()
            destination.save()
            return HttpResponseRedirect('/')
    else:
        form = DestinationForm()
    template = loader.get_template('new_destination.html')
    title = 'Creando un nuevo Destino'
    subtitle = '!Crear Destino! :)'
    context = {
        'form': form,
        'title': title,
        'subtitle': subtitle
    }
    return HttpResponse(template.render(context, request))

class DestinationList(ListView):
    model = Destination

class DestinationDetail(DetailView):
    model = Destination

def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action',None)
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        
        if action == 'login':
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')
    context = {}
    return render(request,'authenticate/login.html',context)

def auth_signup(request):
    if request.method == 'POST':
        action = request.POST.get('action',None)
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        if action == 'signup':
            user = User.objects.create_user(username=username, 
                                        password=password)
            user.save()
    context = {}
    return render (request,'authenticate/signup.html',context)

def auth_logout(request):
    logout(request)
    return redirect('/login')