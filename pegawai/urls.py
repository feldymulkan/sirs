# from django.urls import path
# from . import backup_views

# urlpatterns = [
#     path('', backup_views.list_pegawai, name='list_pegawai'),
#     path("create/", backup_views.create_pegawai, name="create_pegawai"),
#     path('delete/<int:pk>/', backup_views.delete_pegawai, name='delete_pegawai'),
#     path('edit/<int:pk>/', backup_views.edit_pegawai, name='edit_pegawai'),
#     path('toggle-status/<int:pk>', backup_views.toggle_status, name='toggle_status')
    
    
# ]

from django.urls import path
from .views import PegawaiList, DetailPegawai

urlpatterns = [
    path('pegawai/', PegawaiList.as_view(), name='list_pegawai'),
    path('pegawai/<int:pk>/', DetailPegawai.as_view(), name='detail_pegawai'),
    # path('pegawai/<int:pk>/toggle-status/', PegawaiToggleStatusView.as_view(), name='toggle_status_pegawai'),
]

