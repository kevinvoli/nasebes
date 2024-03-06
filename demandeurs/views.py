from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExtraitForm,ReclamationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.

######################################

# HOME OR INDEX VIEW

######################################
# Cette vue homme est la vue principale de tout le site. 
# Son template "main_template" se trouve dans le template principal
def home(request):
    return render(request, "index.html")


######################################

# SERVICES TEMPLATE VIEW

######################################

def services(request):
    return render(request, "services.html" )



######################################

# DEMANDE EXTRAIT VIEW

######################################
def demande_extrait(request):
    message=""
    form = ExtraitForm(request.POST)
    if request.method == "POST":
        form = ExtraitForm(request.POST, request.FILES)
        
        if form.is_valid() and (form.data is not None) :
            
            message = "Vos informations ont été enregistrées avec succès !"

            form.save()
            form = ExtraitForm()
            messages.success(request, message)
            
        else:
            message = "Vos données n'ont pas pu être envoyées !\n Veuillez remplir tout le formulaire."
           
            ExtraitForm()
            messages.error(request, message)
        
    return render(request, "demandeurs/demande_extrait.html" , {'form': form, 'message':message } )


######################################

# VERIFICATION EXTRAIT VIEW

######################################
def verification(request):
    return render(request, "demandeurs/verification.html")


######################################

# RECLAMATION EXTRAIT VIEW

######################################
def reclamation(request):
    message=""
    form = ReclamationForm(request.POST)
    if request.method == "POST":
        form = ReclamationForm(request.POST, request.FILES)
        
        if form.is_valid() and (form.data is not None) :
            
            message = "Votre reclamation a été envoyée avec succès !"

            form.save()
            form = ReclamationForm()
            messages.success(request, message)
            
        else:
            message = "reclamation non envoyés"
           
            ReclamationForm()
            messages.error(request, message)
    return render(request, "demandeurs/reclamation.html",{'form': form, 'message':message })



######################################

# CONTACT VIEW

######################################
def contact(request):
    return render(request, "contact.html")