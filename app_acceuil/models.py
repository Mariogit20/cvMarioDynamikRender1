from django.db import models

# Create your models here.
class Projetscards(models.Model):
    nom = models.CharField(max_length=100 , null=True, blank=True)
    images= models.ImageField(upload_to="static/images/" , null=True, blank=True)
    description= models.TextField( null=True, blank=True)
    # duree = models.IntegerField()
    # date = models.DateField(auto_now_add=True)

# Dates automatiques (utile pour trier vos projets)
    # created_at = models.DateTimeField(auto_now_add=True)
    # Modifiez temporairement comme ceci :
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom if self.nom else f"Projet {self.id}"




# Create your models here.
class Projetsfirstspeciality(models.Model):
    # nom = models.CharField(max_length=100 , null=True, blank=True)
    images= models.ImageField(upload_to="static/images/" , null=True, blank=True)
    description_speciality= models.TextField( null=True, blank=True)
    # duree = models.IntegerField()
    # date = models.DateField(auto_now_add=True)

# Dates automatiques (utile pour trier vos projets)
    # created_at = models.DateTimeField(auto_now_add=True)
    # Modifiez temporairement comme ceci :
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description_speciality if self.description_speciality else f"Projet {self.id}"






# https://gemini.google.com/app/89921fa5ef19a383?hl=fr
# https://gemini.google.com/app/89921fa5ef19a383?hl=fr
# https://gemini.google.com/app/89921fa5ef19a383?hl=fr
# https://gemini.google.com/app/89921fa5ef19a383?hl=fr
# https://gemini.google.com/app/89921fa5ef19a383?hl=fr
    
    
# Lancez python manage.py makemigrations.

#     Lancez python manage.py migrate.

#     Une fois que c'est fait, vous pouvez retirer le null=True et relancer les migrations si vous voulez que le champ soit obligatoire à l'avenir.

# Astuce : Avez-vous déjà des données importantes dans votre base de données, ou êtes-vous encore en phase de test où vous pourriez vous permettre de réinitialiser la base si besoin ?


# ------------------------------------------------------------------





# Autres sources d'erreurs possibles :

#     L'erreur HINT: Get Pillow : Si vous avez un message d'erreur mentionnant Pillow, c'est parce que Django a besoin de cette bibliothèque pour gérer les images.

#         Solution : Tapez      pip install Pillow      dans votre terminal.

#     L'erreur Field 'id' expected a number : Si vous avez ajouté created_at après avoir déjà créé des données, Django peut être confus.

#         Solution : Supprimez les fichiers dans le dossier migrations/ (sauf __init__.py) et relancez :
#         Bash

# python manage.py makemigrations
# python manage.py migrate

# ----------------------------------------------------------------






# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr  


# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr  


# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr  

# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr
# https://gemini.google.com/app/7ef82af70381daf0?hl=fr


# <div class="alert alert-light custom-shadow border-0 rounded-3 p-4 text-center">
#     <p class="mb-0">
#         <i class="bi bi-chat-dots-fill text-primary mb-2 d-block fs-3"></i>
#         Désolé ! Il n'existe aucun témoignage enregistré pour le moment.
#     </p>
# </div>                   


