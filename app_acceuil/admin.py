from django.contrib import admin
from .models import Projetscards , Projetsfirstspeciality
# Register your models here.

class DashProjetsCards(admin.ModelAdmin):
    list_displays=("nom","images","description")



# # Liaison des VARIABLES entre les FICHIERS admin.py ET models.py DANS AppHome    
# class DashLivre(admin.ModelAdmin):
#     list_display = ('titre',)        # TUPLE

# class DashLivreAuteur(admin.ModelAdmin):
#     list_display = ('auteur','livre','date_publication') 



class DashProjetsFirstSpeciality(admin.ModelAdmin):
    list_displays=("images","description_speciality")


# admin.site.register(Projetscards,ActionProjetscards)


modeles = {
    Projetscards:DashProjetsCards,
    Projetsfirstspeciality:DashProjetsFirstSpeciality
}

for model,Dash in modeles.items():
    admin.site.register(model,Dash)

# admin.site.register(Slider,DashSlider)

