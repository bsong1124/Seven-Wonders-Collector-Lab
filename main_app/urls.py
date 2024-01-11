from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wonders/', views.wonders_index, name='index'),
    path('wonders/<int:wonder_id>/', views.wonders_details, name='detail'),
    path('wonders/create/', views.WonderCreate.as_view(), name='wonder_create'),
    path('wonders/<int:pk>/update/', views.WonderUpdate.as_view(), name='wonder_update'),
    path('wonders/<int:pk>/delete/', views.WonderDelete.as_view(), name='wonder_delete')
]