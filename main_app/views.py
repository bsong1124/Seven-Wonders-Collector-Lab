from django.shortcuts import render

wonders = []
# Create your views here.
def home():
    return render('home.html')

def about(request):
    return render('about.html')

def wonders_index(request):
    return render('wonders/index.html',{
        'wonders': wonders
    })