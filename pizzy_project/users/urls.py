from django.urls import path, re_path
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView

from .views import PasswordResetView, PasswordResetConfirmView, LogoutView, SignUpView, Activate, index

app_name = 'users'                            

urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', Activate.as_view(), name='activate'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), 
                                                                name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
                                                                        name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete'),
    path('', index, name='index'),
]