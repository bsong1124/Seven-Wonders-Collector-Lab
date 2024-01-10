from django.shortcuts import render

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
w = Wonder(name='Chicken Itza', country= 'Mexico', year_built='AD 600')
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