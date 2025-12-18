from django.urls import path
from .views import *
urlpatterns = [
    path("",aff_contact,name="name_contact")
]

