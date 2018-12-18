from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Client
from .forms import ClientForm

def show_client(request):
    client = Client.objects.order_by('id')
    template = loader.get_template('clients.html')
    title = 'Clientes Registrados'
    context = {
        'client': client,
        'title': title
    }
    return HttpResponse(template.render(context,request))


def new_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            client.save()
            return HttpResponseRedirect('/clients')
    else:
        form = ClientForm()
    template = loader.get_template('new_client.html')
    title = 'Registrando Cliente'
    context = {
        'form': form,
        'title': title,
    }
    return HttpResponse(template.render(context, request))




