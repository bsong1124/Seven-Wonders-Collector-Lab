from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wonder

# wonders = [
#     {'name': 'Great Wall of China', 'country': 'China'}, '700 BC'
#     {'name': 'Chichen Itza', 'country': 'Mexico'}, 'AD 600'
#     {'name': 'Petra', 'country': 'Jordan'}, "312 BC"
#     {'name': 'Machu Picchu', 'country': 'Peru'}, 'AD 1450'
#     {'name': 'Christ the Redeemer', 'country': 'Brazil'}, 'AD 1931'
#     {'name': 'Taj Mahal', 'country': 'India'}, 'AD 1643'
#     {'name': 'The Colosseum', 'country': 'Italy'},  'AD 80'
#]

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