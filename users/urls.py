from django.urls import path, include
from .views import CustomPasswordResetDoneView
from django.contrib.auth import views as auth_views

from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('accounts/password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),



    # path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
    #     template_name='registration/custom_password_reset_done.html'
    # ), name='password_reset_done'),
]
