from django.urls import path
from . import views 

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('afficher/index/', views.index, name='index'),
    path('formulaire/', views.perso, name ='perso'),
    path('afficher/', views.afficher, name ='afficher'),
]