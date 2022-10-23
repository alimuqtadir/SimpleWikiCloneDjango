from django.urls import path

from . import views


app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title_to_display, name="title_to_display"),
    path("new_page", views.new_page, name="new_page"),
    path("edit_page", views.edit_page, name="edit_page"),
    path("random_entry", views.random_entry, name="random_entry")
]
