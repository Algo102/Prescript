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

from django.conf import settings
from django.conf.urls.static import static
from . import views

# urlpatterns = [
#     path('', views.main, name='main'),
#     path('authorization/', views.authorization, name='authorization'),
#     path('register/', views.register, name='register'),
#     path('logout/', views.user_logout, name='logout'),
#     path('all_receipt/', views.all_receipt, name='all_receipt'),
#     path('get_receipt/', views.get_receipt, name='get_receipt'),
#     path('add_receipt/', views.add_receipt, name='add_receipt'),
#     path('create_category/', views.create_category, name='create_category'),
#     path('receipt_detail/', views.receipt_detail, name='receipt_detail'),
#     path('receipt_detail/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
#     path('modify_receipt/<int:receipt_id>/', views.modify_receipt, name='modify_receipt'),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)