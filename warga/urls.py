# warga/urls.py
from django.urls import path
from .views import (
    WargaListView, WargaDetailView,
    WargaCreateView, WargaUpdateView, WargaDeleteView,
    PengaduanListView, PengaduanCreateView, PengaduanUpdateView, PengaduanDeleteView
)

app_name = 'warga'

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),

    # pengaduan
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    # Tambahkan di bawah URL pengaduan lainnya
path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),

]
