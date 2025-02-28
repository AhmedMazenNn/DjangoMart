from django.urls import path

from home.views import get_home_page, projects , contact ,welcome

urlpatterns = [
    path("home/", get_home_page),
    path("projects/", projects),
    path("contact/" , contact),
    path("welcome/" , welcome)
]
