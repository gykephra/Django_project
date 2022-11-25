from multiprocessing import context
from django.shortcuts import render 
from django.http import HttpResponse 
from .models import Personnes
from .forms import PersonneForm

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



def perso(request):
    context = {
        'page_title' : "Formulaire de soumission d'annonces",
        
    }

    if request.method == 'POST':

        # POST, generate form with data from the request
        form = PersonneForm(request.POST)
        # check if we get data
        print("data", form.data)
        # check if it's valid:
        if form.is_valid():
            form_lastname = form.cleaned_data['nom']
            form_firstname = form.cleaned_data['prenom']
            form_city = form.cleaned_data['ville']
            form_age = form.cleaned_data['age']
            form_comment = form.cleaned_data['commentaire']
            form_photo = form.cleaned_data['photo']
            context['formInfo'] = {Personnes.objects.all()}
            context['btnFormHidden'] = True # To hide the button is the form is successfully submitted
            # print the values to make sure their are correct
            print(context['formInfo'])
            return render(request, 'fichiers/afficher.html', context)
        else:
             # print the errors, just in case
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'fichiers/formulaire_personnes.html', context)

    else:
        # GET, generate blank form
        context['form'] = PersonneForm()
    return render(request, 'fichiers/formulaire_personnes.html', context)

def afficher(request):
    context = {
        'formInfo' : Personnes.objects.all(),
        }
    return render(request, 'fichiers/afficher.html', context)