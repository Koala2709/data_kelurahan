from django.urls import path
from .views import (
    WargaListView, WargaDetailView,
    WargaCreateView, WargaUpdateView, WargaDeleteView, PengaduanListView, PengaduanCreateView
)

app_name = 'warga'

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('tambah/', WargaCreateView.as_view(), name='warga-add'),
    path('ubah/<int:pk>/', WargaUpdateView.as_view(), name='warga-edit'),
    path('hapus/<int:pk>/', WargaDeleteView.as_view(), name='warga-delete'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
]
