from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wonder

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wonders_index(request):
    wonders = Wonder.objects.all()
    return render(request, 'wonders/index.html',{
        'wonders': wonders
    })

def wonders_details(request, wonder_id):
    wonder = Wonder.objects.get(id=wonder_id)
    return render(request, 'wonders/details.html', {
        'wonder': wonder
    })

class WonderCreate(CreateView):
    model = Wonder
    fields = '__all__'

class WonderUpdate(UpdateView):
    model = Wonder
    fields = '__all__'

class WonderDelete(DeleteView):
    model = Wonder
    success_url = '/wonders'