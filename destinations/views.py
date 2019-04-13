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

#generic class based views
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.views.generic import ListView
#import auth
from django.contrib.auth import (
    authenticate, 
    login, 
    logout
)
from django.contrib.auth.models import User
from .mixins import LoginRequiredMixin

# Create your views here.

class DestinationNew(CreateView):
    model = Destination
    fields = ['name', 'description', 'itinerary', 'category' ,'price', 'image']
    success_url = reverse_lazy('destinations_app:show_destination')

class DestinationDetail(LoginRequiredMixin, DetailView):
    model = Destination

class DestinationList(ListView):
    model = Destination

class DestinationUpdate(UpdateView):
    model = Destination
    fields = ['name', 'description', 'itinerary', 'category', 'price', 'image']
    success_url = reverse_lazy('destinations_app:show_destination')


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