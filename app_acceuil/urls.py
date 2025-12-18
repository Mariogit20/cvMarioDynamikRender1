from django.urls import path
from .views import *
urlpatterns = [
    path("",aff_acceuil,name="name_acceuil")
]
