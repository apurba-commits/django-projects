from django.urls import path
from .views import home, add_note,delete_note

urlpatterns = [
    path("", home, name="home"),
    path("add/", add_note, name="add_note"),
    path("delete/<int:note_id>/", delete_note, name="delete_note"),
]
