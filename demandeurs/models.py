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
        # ABOBO = 'ABOB', 'ABOBO'
        # ADJAME = 'ADJA', 'ADJAME'
       # ODIENNE = 'ODIE', 'ODIENNE'
        	
           abengourou	= 'ABEN', 'abengourou' 	
           abobo	 	= 'ABOB', 'ABOBO'
           aboisso	 	= 'ABOI', 'ABOISSO'
           adiake	 	= 'ADIA', 'ADIAKE'
           adjame      = 'ADJA', 'ADJAME'
           adzope	 	= 'ADZO', 'ADZOPE'
           affery	 	= 'AFFE', 'AFFERY'
           agboville	= 'AGBO', 'AGBOVILLE'	
           agnibilekro	 = 'AGNI', 'AGNIBILEKRO'
           agou          = 'AGO', 'AGOU'
           akoupe	 	   = 'AKOU', 'AKOUPE'
           alepe	 	   = 'ALE', 'ALEPE'
           anoumaba	 	= 'ANOU', 'ANOUMABA'
           anyama	 	    = 'ANY', 'ANYAMA'
           arrah          = 'ARRA', 'ARRAH'
           assinie_mafia	= 'ASSI', 'ASSINIE_MAFIA'	
           assuefry	 	= 'ASSUE', 'ASSUEFRY'
           attecoube	 	= 'ATTE', 'ATTECOUBE'
           attiegouakro	 = 'ATTIE', 'ATTIEGOUAKRO'	
           bingerville     = 'bing', 'BINGERVILLE'
           odienne         = 'ODIE', 'ODIENNE'


# (20) ayame
 
# (21) azaguie	 	
# (22) bako	 	
# (23) bangolo	 	
# (24) bassawa	 	
# (25) bediala
 
# (26) beoumi	 	
# (27) bettie	 	

# (28) biankouma	 	
# (29) bingerville	 	
# (30) binhouye
 
# (31) blolequin	 	
# (32) bocanda	 	
# (33) bodokro	 	
# (34) bondoukou	 	
# (35) bongouanou
 
# (36) bonieredougou	 	
# (37) bonon	 	
# (38) bonoua	 	
# (39) booko	 	
# (40) borotou
 
# (41) botro	 	
# (42) bouafle	 	
# (43) bouake	 	
# (44) bouna	 	
# (45) boundiali
 
# (46) brobo	 	
# (47) buyo	 	
# (48) cocody	 	
# (49) dabakala	 	
# (50) dabou
 
# (51) daloa	 	
# (52) danane	 	
# (53) daoukro	 	
# (54) diabo	 	
# (55) dianra
 
# (56) diawala	 	
# (57) didievi	 	

# (58) diegonefla	 	
# (59) dikodougou	 	
# (60) dimbokro
 
# (61) dioulatiedougou	 	
# (62) divo	 	
# (63) djebonoua	 	
# (64) djekanou	 	
# (65) djibrosso
 
# (66) doropo	 	
# (67) dualla	 	
# (68) duekoue	 	
# (69) ettrokro	 	
# (70) facobly
 
# (71) ferkessedougou	 	
# (72) foumbolo	 	
# (73) fresco	 	
# (74) fronan	 	
# (75) gagnoa
 
# (76) gbeleban	 	
# (77) gboguhe	 	
# (78) gbon	 	
# (79) gbonne	 	
# (80) gohitafla
 
# (81) goulia	 	
# (82) grabo	 	
# (83) grand bassam	 	
# (84) grand bereby	 	
# (85) grand lahou
 
# (86) grand zattry	 	
# (87) gueyo	 	
# (88) guiberoua	 	
# (89) guiembre	 	
# (90) guiglo
 
# (91) guinteguela	 	
# (92) guitry	 	
# (93) hire	 	
# (94) issia	 	
# (95) jacqueville
 
# (96) kanakono	 	
# (97) kani	 	
# (98) kaniasso	 	
# (99) karakoro	 	
# (100) kassere
 
# (101) katiola	 	
# (102) kokoumbo	 	
# (103) kolia	 	
# (104) komborodougou	 	
# (105) kong
 
# (106) kongasso	 	
# (107) koonan	 	
# (108) korhogo	 	
# (109) koro	 	
# (110) kouassi dattekro
 
# (111) kouassi kouassikro	 	
# (112) kouibly	 	
# (113) koumassi	 	
# (114) koumbala	 	
# (115) koun fao
 
# (116) kounahiri	 	
# (117) kouto	 	
# (118) lakota	 	
# (119) logouale	 	
# (120) mbahiakro
 
# (121) mbatto	 	
# (122) mbengue	 	
# (123) madinani	 	
# (124) mafere	 	
# (125) man
 
# (126) mankono	 	
# (127) marcory	 	
# (128) massala	 	
# (129) mayo	 	
# (130) meagui
 
# (131) minignan	 	
# (132) morondo	 	
# (133) ndouci	 	
# (134) napie	 	
# (135) nassian
 
# (136) niable	 	
# (137) niakaramadougou	 	
# (138) nielle	 	
# (139) niofoin	 	
# (140) odienne
 
# (141) ouangolodougou	 	
# (142) ouaninou	 	
# (143) ouelle	 	
# (144) oume	 	
# (145) ouragahio
 
# (146) plateau	 	
# (147) port bouet	 	
# (148) prikro	 	
# (149) rubino	 	
# (150) saioua
 
# (151) sakassou	 	
# (152) samatiguila	 	
# (153) san pedro	 	
# (154) sandegue	 	
# (155) sangouine
 
# (156) sarhala	 	
# (157) sassandra	 	
# (158) satama sokoro	 	
# (159) satama sokoura	 	
# (160) seguela
 
# (161) seguelon	 	
# (162) seydougou	 	
# (163) sifie	 	
# (164) sikensi	 	
# (165) sinematiali
 
# (166) sinfra	 	
# (167) sipilou	 	
# (168) sirasso	 	
# (169) songon	 	
# (170) soubre
 
# (171) taabo	 	
# (172) tabou	 	
# (173) tafire	 	
# (174) tai	 	
# (175) tanda
 
# (176) tehini	 	
# (177) tengrela	 	
# (178) tiapoum	 	
# (179) tiassale	 	
# (180) tie n?diekro
 
# (181) tiebissou	 	
# (182) tieme	 	

# (183) tiemelekro	 	
# (184) tieningboue	 	
# (185) tienko
 
# (186) tioroniaradougou	 	
# (187) tortiya	 	
# (188) touba	 	
# (189) toulepleu	 	
# (190) toumodi
 
# (191) transua	 	
# (192) treichville	 	
# (193) vavoua	 	
# (194) worofla	 	
# (195) yakasse attobrou
 
# (196) yamoussoukro	 	
# (197) yopougon	 	
# (198) zikisso	 	
# (199) zouan hounien	 	
# (200) zoukougbeu
 
# (201) zuenoula
    
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