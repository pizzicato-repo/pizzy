from django.urls import path

from .views import ProfileView, AccueilView, LB_create, LB_detail


app_name = 'app1'
urlpatterns = [
    path('', AccueilView.as_view(), name='accueil'),

    path('accounts/profile/', ProfileView.as_view(), name='profile'),

    path('create-lb/', LB_create.as_view(), name='create-lb'),
    path('detail-lb/<int:pk>/', LB_detail.as_view(), name='detail-lb'),

]    