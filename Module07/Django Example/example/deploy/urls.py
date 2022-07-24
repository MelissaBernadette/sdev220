from django.urls import path
from . import views

urlpatterns = [
    path("homePage/", views.Home),
    path("otherPage/", views.Other),
    path("post_list/", views.post_list)
]

