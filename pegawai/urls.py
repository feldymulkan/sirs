from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_pegawai, name='list_pegawai'),
    path("create/", views.create_pegawai, name="create_pegawai"),
    path('delete/<int:pk>/', views.delete_pegawai, name='delete_pegawai'),
    path('edit/<int:pk>/', views.edit_pegawai, name='edit_pegawai'),
    path('toggle-status/<int:pk>', views.toggle_status, name='toggle_status')
    
    
]
