from django.shortcuts import render
from .models import Contact

# Create your views here.
def aff_contact(request):
    listeContact = Contact.objects.all()
    contenu = {
        "formation":listeContact
    }
    return render(request,"index.html", contenu)

