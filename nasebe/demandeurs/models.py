from django.db import models
from django import forms
from django.urls import reverse
from model_utils import Choices



# Create your models here.

######################################

# EXTRAIT MODEL

######################################
CHOICES = (
        ('', 'Choose..'),
        ('1','Abobo'), 
        ('2','Adjame'), 
        ('3','Korhgo'),
        )

class ExtraitModel(models.Model):
    class MairieChoices(models.TextChoices):
        ABOBO = 'ABOB', 'ABOBO'
        ADJAME = 'ADJA', 'ADJAME'
        ODIENNE = 'ODIE', 'ODIENNE'
    
    id = models.AutoField(primary_key=True)    
    Nom=models.CharField(max_length=100)
    Prenoms=models.CharField(max_length=100,)
    Date_de_naissance =models.DateField()
    Lieu_de_naissance= models.CharField(max_length=100,blank=False, null=False)
    Numero_acte_de_naissance=models.CharField(max_length=100,blank=False, null=False)    
    Ville_de_residence=models.CharField(max_length=100,blank=False, null=False)
    Nom_et_prenoms_du_pere = models.CharField(max_length=100,blank=False, null=False)
    Nom_et_prenoms_de_la_mere = models.CharField(max_length=100,blank=False, null=False)
    Mairie_de_demande = models.CharField( max_length=100, choices=MairieChoices.choices, blank=False, null=False)    
    Nombre_de_copie=models.IntegerField(blank=False, null=False)    
    Telephone=models.CharField (max_length=10,blank=False, null=False)
    Email=models.EmailField(blank=False, null=False)

    STATUS = 'NON_TRAITE'
    status = models.CharField(default=STATUS, max_length=20)
    
    slug  = models.SlugField(max_length=128)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Photocopie_d_extrait = models.FileField(upload_to='extraits', blank=True, null=True)

    def __str__(self):
        return self.Nom
    
    
    
    
######################################

# VALIDATION MODEL

######################################
class ValidationModel(models.Model):
    
    id = models.AutoField(primary_key=True)
    STATUS = Choices('NON_TRAITE', 'ACCEPTE','REFUSE', 'DELIVRE')
    status = models.CharField(choices=STATUS, default=STATUS.NON_TRAITE, max_length=20)
    
    def __str__(self):
        return self.status
    
    

######################################

# RECLAMATION MODEL

######################################
class ReclamationModel(models.Model):
        
    id = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=130)
    Prenoms = models.CharField(max_length=130)
    Telephone = models.CharField(max_length=130)
    Message=models.CharField(max_length=98999)

    def __str__(self):
        return self.Nom
    
    
######################################

# CONTACT MODEL

######################################
class ContactModel(models.Model):
        
    id = models.AutoField(primary_key=True)
    Nom=models.CharField(max_length=100)
    Prenoms=models.CharField(max_length=100)
    Telephone = models.CharField(max_length=130)
    Objet=models.CharField(max_length=100)
    Message=models.CharField(max_length=98999)

    def __str__(self):
        return self.Nom