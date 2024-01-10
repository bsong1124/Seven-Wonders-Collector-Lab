from django.urls import path
from . import views

urlpatterns = {
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wonders/', views.wonders_index, name='index'),
    path('wonders/<int:wonder_id', views.wonders_details, name='detail')
}