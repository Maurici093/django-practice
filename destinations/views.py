from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Destination
from .forms import DestinationForm

# Create your views here.

def show_destination(request):
    destination = Destination.objects.order_by('id')
    template = loader.get_template('index.html')
    page_title = 'Ecoturismo En Colombia - Native Colombia - Agencia especializada'
    context = {
        'destination': destination,
        'page_title': page_title
    }
    return HttpResponse(template.render(context,request))

'''def saludo(request):
    template = loader.get_template('saludo.html')
    big_title = 'Este es el titulo del header'
    title = 'Vive una Experiencia Natural'
    context = {
        'big_title': big_title,
        'title': title
    }
    return HttpResponse(template.render(context, request))'''

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    template = loader.get_template('destination_detail.html')
    title = 'Descripción - Destino:'
    context = {
        'destination': destination,
        'title': title
    }
    return HttpResponse(template.render(context,request))

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