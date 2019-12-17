from django.urls import path

from .views import ProfileView


app_name = 'app1'
urlpatterns = [
    path('accounts/profile/', ProfileView.as_view(), name='profile'),

]    