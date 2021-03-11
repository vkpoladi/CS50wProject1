from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new", views.new, name="new"),
    path("edit/<str:heading>", views.edit, name="edit"),

    # Alternatively, if we don't want to pass in 'heading' via URL:
    # Can pass in 'heading' through submit button value i.e. value="{{ heading }}"
    # Then pagename = request.POST.get("edit")
    # This would allow edit function to only have 1 argument (request)

    path("save/<str:title>", views.save, name="save")
]