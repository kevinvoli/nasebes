from django.forms import ModelForm, fields
from django.forms.models import fields_for_model
from .models import ExtraitModel, ContactModel,ReclamationModel
from django import forms



######################################

# EXTRAIT FORM

######################################
CHOICES  = ExtraitModel.MairieChoices.choices

class ExtraitForm(ModelForm):
    
    Nom=forms.CharField(
        max_length=100,
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Votre nom'}) 
        )
    Prenoms=forms.CharField(
        max_length=100,
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Vos prenoms'}) 
        )
    Date_de_naissance =forms.DateField(
        required=True,
        localize=True,
        widget=forms.DateInput(attrs={'placeholder': 'Date de naissance', 'type':'date'}) ,
        label= 'Date de naissance : '
    )
    Lieu_de_naissance= forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Lieu de naissance'}) ,
        label= 'Lieu de naissance : '
        )
    Numero_acte_de_naissance=forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Numéro acte de naissance'}),
        label='Numero d\'acte de naissance : '
        )    
    Ville_de_residence=forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ville de résidence'}),
        label='Ville de résidence : '
        )
    Nom_et_prenom_du_pere = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nom et prénoms du père'}),
        label='Nom et prénoms du père : '
        )
    Nom_et_prenom_de_la_mere = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nom et prénoms de la mère'}),
        label='Nom et prénoms de la mère : ' 
        
        )
    Mairie_de_demande = forms.ChoiceField(
        widget=forms.Select(attrs={'placeholder': 'Choisir la commune',  'name':'select', 'class':'regDropDown'}), 
        choices=CHOICES,
        label='Mairie de la démande'
        )        
    Nombre_de_copie=forms.IntegerField(
        required=True,
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Nombre de copie'}),
        label='Nombre de copie(s)'
        )        
    Telephone=forms.CharField (
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Téléphone'}),
         label='Téléphone'
        )
    Email=forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Votre email'}),
        label="Email" 
        )
    
    Photocopie_d_extrait=forms.FileField(
        
        max_length=100,
        required=False,
        widget=forms.FileInput(attrs={'placeholder': 'Votre email'}),
        label='Photocopie de votre extrait',
        )
    
    
    class Meta: 
        model = ExtraitModel
        fields = [ 'id', 'Nom','Prenoms','Date_de_naissance', 'Lieu_de_naissance', 'Numero_acte_de_naissance','Ville_de_residence', 
                  'Nom_et_prenom_du_pere', 'Nom_et_prenom_de_la_mere', 'Mairie_de_demande',
                  'Nombre_de_copie','Telephone','Email', 'Photocopie_d_extrait' ]
 
 
 
 

######################################

# CONTACT FORM

######################################
class ContactForm(ModelForm):
    
    Nom=forms.CharField(max_length=100,required=True)
    Prenoms=forms.CharField(max_length=100,required=True)
    Telephone = forms.CharField(max_length=130)
    Objet=forms.CharField(max_length=100,required=True)
    Message=forms.CharField(max_length=98999,required=True)
    class Meta: 
        model = ContactModel
        fields = [ 'id', 'Nom','Prenoms','Telephone','Objet','Message']
        
        
class ReclamationForm(ModelForm):
    
    Nom=forms.CharField(max_length=100,required=True)
    Prenoms=forms.CharField(max_length=100,required=True)
    Telephone = forms.CharField(max_length=130)
  
    Message=forms.CharField(max_length=98999,required=True)
    class Meta: 
        model = ReclamationModel
        fields = [ 'id', 'Nom','Prenoms','Telephone','Message']  
        