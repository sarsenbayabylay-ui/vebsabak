from django.urls import path
from . import views

urlpatterns = [
    path("", views.ticket_list_and_create, name="ticket_list"),
]