from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, LoginForms
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.

from.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.forms.widgets import PasswordInput
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import  get_object_or_404,render,redirect
from django import forms
from django.template import loader

from.forms import UserRegisterForm
from django.shortcuts import render
from django.contrib.auth import authenticate,login
# from .forms import  LoginForms
from django .http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from demandeurs.models import ExtraitModel


######################################

# LOGIN AND REGISTER VIEW

######################################

# Inscription
def inscription_mairie(request):
    if request.method =="POST":
        form=UserRegisterForm(request.POST)
        
        if form.is_valid():
            eng = form.save()
            
            username=form.cleaned_data.get('userneme')
            messages.success(request,f'Salut ,{eng.username}, votre compte a été créé avec succès',)
            
            return redirect('espacemairie')

    else:
        form = UserRegisterForm()

    return render(request, 'mairies/inscription_mairie.html', {'form':form})


# Connexion
def connexion_mairie(request):
    if request.method== 'POST':
        form=LoginForms(request.POST)

        if form.is_valid():
            cd= form.cleaned_data
            user= authenticate(request, username= cd['username'],
            Password=cd['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponse('AUTHENTIFICATION WAS SUCCESSFULL')

            else:
                return  HttpResponse('AUTHENTIFICATION FAILLED TRY AGAIN ')
    else:
        form=LoginForms()

    return render(request, 'mairies/connexion_mairie.html', {'form':form})


# Changer le mot de passe.
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'mairies/change_password.html', {
        'form': form
    })



######################################

# DASHBORD AND ESPACE MAIRIE VIEWS

######################################
@login_required
def user(request):
    return render(request, "mairies/espacemairie.html" )


@login_required
def espacemairie(request):
    # nombre= ExtraitModel.objects.filter(Mairie_de_demande="ABOB").count()
    datatabobo = ExtraitModel.objects.filter(Mairie_de_demande="ABOB")
    datatabobolimit = ExtraitModel.objects.filter(Mairie_de_demande="ABOB")[:5]
    nouvelle_demande_abobo =datatabobo.filter(status= "NON_TRAITE").count()
    nombre_demande_accepte_abobo =datatabobo.filter(status= "ACCEPTE").count()
    nombre_demande_refuse_abobo =datatabobo.filter(status= "REFUSE").count()
    nombre_demande_livre_abobo =datatabobo.filter(status= "DELIVRE").count()
    historique_demande_abobo = ExtraitModel.objects.filter(Mairie_de_demande="ABOB").count()
    pourcentage_nouvelle_demande= round( (nouvelle_demande_abobo * 100)/(historique_demande_abobo) )
    pourcentage_accepte_demande= round((nombre_demande_accepte_abobo * 100)/(historique_demande_abobo)) 
    pourcentage_refuse_demande= round((nombre_demande_refuse_abobo * 100)/(historique_demande_abobo))
    pourcentage_livre_demande= round((nombre_demande_livre_abobo * 100)/(historique_demande_abobo))
    
    
    dict2={
        "nombre_demande_accepte_abobo":nombre_demande_accepte_abobo,
        "nombre_demande_refuse_abobo":nombre_demande_refuse_abobo,
        "nombre_demande_livre_abobo":nombre_demande_livre_abobo,
        "nouvelle_demande_abobo":nouvelle_demande_abobo,
        "historique_demande_abobo":historique_demande_abobo,
        "pourcentage_nouvelle_demande":pourcentage_nouvelle_demande,
        "pourcentage_accepte_demande":pourcentage_accepte_demande,
        "pourcentage_refuse_demande":pourcentage_refuse_demande,
        "pourcentage_livre_demande":pourcentage_livre_demande,
        "datatabobo":datatabobo,
        "datatabobolimit":datatabobolimit,
        
    }
    
    return render(request,"mairies/espacemairie.html",dict2)



# Liste des demandes d'extrait par mairie.

def demande_accepte(request):
    
        # nombre= ExtraitModel.objects.filter(Mairie_de_demande="ABOB").count()
    datatabobo = ExtraitModel.objects.filter(Mairie_de_demande="ABOB")
    datatabobolimit = ExtraitModel.objects.filter(Mairie_de_demande="ABOB")[:5]
    nouvelle_demande_abobo =datatabobo.filter(status= "NON_TRAITE").count()
    nombre_demande_accepte_abobo =datatabobo.filter(status= "ACCEPTE").count()
    nombre_demande_refuse_abobo =datatabobo.filter(status= "REFUSE").count()
    nombre_demande_livre_abobo =datatabobo.filter(status= "DELIVRE").count()
    historique_demande_abobo = ExtraitModel.objects.filter(Mairie_de_demande="ABOB").count()
    pourcentage_nouvelle_demande= round( (nouvelle_demande_abobo * 100)/(historique_demande_abobo) )
    pourcentage_accepte_demande= round((nombre_demande_accepte_abobo * 100)/(historique_demande_abobo)) 
    pourcentage_refuse_demande= round((nombre_demande_refuse_abobo * 100)/(historique_demande_abobo))
    pourcentage_livre_demande= round((nombre_demande_livre_abobo * 100)/(historique_demande_abobo))
    
    
    dict2={
        "nombre_demande_accepte_abobo":nombre_demande_accepte_abobo,
        "nombre_demande_refuse_abobo":nombre_demande_refuse_abobo,
        "nombre_demande_livre_abobo":nombre_demande_livre_abobo,
        "nouvelle_demande_abobo":nouvelle_demande_abobo,
        "historique_demande_abobo":historique_demande_abobo,
        "pourcentage_nouvelle_demande":pourcentage_nouvelle_demande,
        "pourcentage_accepte_demande":pourcentage_accepte_demande,
        "pourcentage_refuse_demande":pourcentage_refuse_demande,
        "pourcentage_livre_demande":pourcentage_livre_demande,
        "datatabobo":datatabobo,
        "datatabobolimit":datatabobolimit,
        
    }

    dict1={'dataExtraitabobo' : ExtraitModel.objects.all()}
    return render(request, "mairies/demande_accepte.html" , dict2 )


def demande_refuse(request): 
    
    datatabobo = ExtraitModel.objects.filter(Mairie_de_demande="ABOB")
    datatabobolimit = ExtraitModel.objects.filter(Mairie_de_demande="ABOB")[:5]
    nouvelle_demande_abobo =datatabobo.filter(status= "NON_TRAITE").count()
    nombre_demande_accepte_abobo =datatabobo.filter(status= "ACCEPTE").count()
    nombre_demande_refuse_abobo =datatabobo.filter(status= "REFUSE").count()
    nombre_demande_livre_abobo =datatabobo.filter(status= "DELIVRE").count()
    historique_demande_abobo = ExtraitModel.objects.filter(Mairie_de_demande="ABOB").count()
    pourcentage_nouvelle_demande= round( (nouvelle_demande_abobo * 100)/(historique_demande_abobo) )
    pourcentage_accepte_demande= round((nombre_demande_accepte_abobo * 100)/(historique_demande_abobo)) 
    pourcentage_refuse_demande= round((nombre_demande_refuse_abobo * 100)/(historique_demande_abobo))
    pourcentage_livre_demande= round((nombre_demande_livre_abobo * 100)/(historique_demande_abobo))
    
    
    dict2={
        "nombre_demande_accepte_abobo":nombre_demande_accepte_abobo,
        "nombre_demande_refuse_abobo":nombre_demande_refuse_abobo,
        "nombre_demande_livre_abobo":nombre_demande_livre_abobo,
        "nouvelle_demande_abobo":nouvelle_demande_abobo,
        "historique_demande_abobo":historique_demande_abobo,
        "pourcentage_nouvelle_demande":pourcentage_nouvelle_demande,
        "pourcentage_accepte_demande":pourcentage_accepte_demande,
        "pourcentage_refuse_demande":pourcentage_refuse_demande,
        "pourcentage_livre_demande":pourcentage_livre_demande,
        "datatabobo":datatabobo,
        "datatabobolimit":datatabobolimit,
        
    }
    return render(request, "mairies/demande_refuse.html" , dict2)

def nouvelle_demande(request): 
    
    datatabobo = ExtraitModel.objects.filter(Mairie_de_demande="ABOB")
    datatabobolimit = ExtraitModel.objects.filter(Mairie_de_demande="ABOB")[:5]
    nouvelle_demande_abobo =datatabobo.filter(status= "NON_TRAITE").count()
    nombre_demande_accepte_abobo =datatabobo.filter(status= "ACCEPTE").count()
    nombre_demande_refuse_abobo =datatabobo.filter(status= "REFUSE").count()
    nombre_demande_livre_abobo =datatabobo.filter(status= "DELIVRE").count()
    historique_demande_abobo = ExtraitModel.objects.filter(Mairie_de_demande="ABOB").count()
    pourcentage_nouvelle_demande= round( (nouvelle_demande_abobo * 100)/(historique_demande_abobo) )
    pourcentage_accepte_demande= round((nombre_demande_accepte_abobo * 100)/(historique_demande_abobo)) 
    pourcentage_refuse_demande= round((nombre_demande_refuse_abobo * 100)/(historique_demande_abobo))
    pourcentage_livre_demande= round((nombre_demande_livre_abobo * 100)/(historique_demande_abobo))
    
    
    dict2={
        "nombre_demande_accepte_abobo":nombre_demande_accepte_abobo,
        "nombre_demande_refuse_abobo":nombre_demande_refuse_abobo,
        "nombre_demande_livre_abobo":nombre_demande_livre_abobo,
        "nouvelle_demande_abobo":nouvelle_demande_abobo,
        "historique_demande_abobo":historique_demande_abobo,
        "pourcentage_nouvelle_demande":pourcentage_nouvelle_demande,
        "pourcentage_accepte_demande":pourcentage_accepte_demande,
        "pourcentage_refuse_demande":pourcentage_refuse_demande,
        "pourcentage_livre_demande":pourcentage_livre_demande,
        "datatabobo":datatabobo,
        "datatabobolimit":datatabobolimit,
        
    }
    return render(request, "mairies/nouvelle_demandes.html" , dict2)

@login_required
def accepte(request, id):
    demande = ExtraitModel.objects.get(id=id)
    
    context ={}

    if request.method =="POST":
        demande.status="ACCEPTE"
        demande.save()
        
            
        return HttpResponseRedirect("../../nouvelle_demande")
    
    return render(request, "mairies/accepte.html", context)

@login_required
def refuse(request, id):
    demande = ExtraitModel.objects.get(id=id)
    
    context ={}
    
    

    if request.method =="POST":
        demande.status="REFUSE"
        demande.save()
       
            
        return HttpResponseRedirect("../../nouvelle_demande")
    
    return render(request, "mairies/refuse.html", context)