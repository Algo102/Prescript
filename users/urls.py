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


# from .views import CustomPasswordResetView, CustomPasswordResetDoneView
#
# urlpatterns = [
#    path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
# ]

# from django.contrib.auth import views as auth_views
#
# urlpatterns = [
#     # ... другие URL-шаблоны ...
#     path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
#         template_name='registration/password_reset_form.html',
#         email_template_name='registration/password_reset_email.html',
#         subject_template_name='registration/password_reset_subject.txt'
#     ), name='password_reset'),
# ]

