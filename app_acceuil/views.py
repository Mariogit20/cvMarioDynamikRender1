from django.shortcuts import render
from .models import Projetscards, Projetsfirstspeciality

def aff_acceuil(request):
    # 1. Gestion des Témoignages
    temoignages = Projetscards.objects.all()
    
    # 2. Gestion de la Spécialité
    specialites = Projetsfirstspeciality.objects.all()
    # Si vous voulez seulement la première : 
    # premiere_spec = Projetsfirstspeciality.objects.first()

    # 3. Regroupement dans un contexte UNIQUE
    contenu = {
        # Données témoignages
        "TEMOIGNAGES_des_PERSONNES_cards": temoignages,
        "EXISTENCE_de_TEMOIGNAGES": temoignages.exists(),
        
        # Données spécialités
        "AFFICHER_la_PREMIERE_SPECIAISATION": specialites,
        "EXISTENCE_de_PREMIERE_SPECIAISATION": specialites.exists(),
    }

    # 4. Un seul render avec toutes les données
    return render(request, "index.html", contenu)




# https://gemini.google.com/app/17a2be2e2e7ab153?hl=fr
# https://gemini.google.com/app/17a2be2e2e7ab153?hl=fr
# https://gemini.google.com/app/17a2be2e2e7ab153?hl=fr
# https://gemini.google.com/app/17a2be2e2e7ab153?hl=fr



# https://gemini.google.com/app/89921fa5ef19a383?hl=fr
# https://gemini.google.com/app/89921fa5ef19a383?hl=fr
# https://gemini.google.com/app/89921fa5ef19a383?hl=fr
# https://gemini.google.com/app/89921fa5ef19a383?hl=fr



# Pourquoi c'est mieux ainsi ?

#     Performance : temoignages.exists() est très rapide car il ne récupère pas toutes les données de la base, il vérifie juste si une ligne existe.

#     Lisibilité : Le code est direct et facile à maintenir.

#     Template : Dans votre fichier index.html, vous pouvez maintenant faire une boucle simple :
    
    