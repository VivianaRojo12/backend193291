from django.urls import path, re_path

from Profile import views

urlspatterns = [
    re_path(r'^profileModel_url', views.ProfileModelView.as_view())
]