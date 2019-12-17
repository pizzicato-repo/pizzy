from django.urls import path

from .views import ProfileView, AccueilView


app_name = 'app1'
urlpatterns = [
    path('', AccueilView.as_view(), name='accueil'),

    path('accounts/profile/', ProfileView.as_view(), name='profile'),


]    