"""
URL configuration for nasebe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demandeurs.views import home
from mairies.views import inscription_mairie, connexion_mairie, espacemairie, change_password, demande_accepte, demande_refuse,nouvelle_demande,accepte,refuse
from demandeurs.views import services
from demandeurs.views import demande_extrait, verification, reclamation, contact
from django.contrib.auth import views as auth_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 



urlpatterns = [
    
    path('', home, name='home'), # vue principale du site
    path('admin/', admin.site.urls),
    path('services', services, name='services'), # vue services du site
    path('contact', contact, name='contact'), # vue services du site
    
    # liens vers les vues de l'application demandeurs
    path('connexion_mairie', auth_view.LoginView.as_view(template_name='mairies/connexion_mairie.html'), name='connexion_mairie'), 
    path('inscription_mairie', inscription_mairie, name='inscription_mairie'), 
    path('change_password', change_password, name='change_password'), 
    path("logout",auth_view.LogoutView.as_view(template_name='index.html'), name="logout" ),
    
    
    path('espacemairie', espacemairie, name='espacemairie'), 
    path("demande_accepte",demande_accepte, name="demande_accepte" ),
    path("demande_refuse",demande_refuse, name="demande_refuse" ),
    path("nouvelle_demande",nouvelle_demande, name="nouvelle_demande" ),
    
    
    
    
    path('demande_extrait', demande_extrait, name='demande_extrait'), 
    path('verification', verification, name='verification'), 
    path('reclamation', reclamation, name='reclamation'), 
    path("<id>/accepte",accepte, name="accepte" ),
    path("<id>/refuse",refuse, name="refuse" ),
    
    
    
    

]
