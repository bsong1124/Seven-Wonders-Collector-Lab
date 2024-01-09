from django.shortcuts import render

wonders = [
    {'name': 'Great Wall of China', 'country': 'China'},
    {'name': 'Chichen Itza', 'country': 'Mexico'},
    {'name': 'Petra', 'country': 'Jordan'},
    {'name': 'Machu Picchu', 'country': 'Peru'},
    {'name': 'Christ the Redeemer', 'country': 'Brazil'},
    {'name': 'Taj Mahal', 'country': 'India'},
    {'name': 'The Colosseum', 'country': 'Italy'},  
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wonders_index(request):
    return render(request, 'wonders/index.html',{
        'wonders': wonders
    })