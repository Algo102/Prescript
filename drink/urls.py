from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='main'),
    path('create_category/', views.create_category, name='create_category'),
    path('receipt_detail/', views.receipt_detail, name='receipt_detail'),
    path('add_receipt/', views.add_receipt, name='add_receipt'),
    path('all_receipt/', views.all_receipt, name='all_receipt'),
    path('get_receipt/', views.get_receipt, name='get_receipt'),
    path('receipt_detail/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('modify_receipt/<int:receipt_id>/', views.modify_receipt, name='modify_receipt'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


