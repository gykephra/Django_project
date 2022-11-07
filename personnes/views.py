from multiprocessing import context
from django.shortcuts import render 
from django.http import HttpResponse 

personne = {
    'first_name' : "",
    'last_name' : ""
} 

def index(request):
    context = {
        'title_page' : "acceuil",
        'user': personne ,
    }
    return render(request, 'fichiers/index.html', context)