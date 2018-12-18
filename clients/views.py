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


