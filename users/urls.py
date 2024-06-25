from django.urls import path, include
from .views import CustomPasswordResetDoneView

from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
]


