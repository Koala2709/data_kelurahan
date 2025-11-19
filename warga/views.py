from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
from rest_framework.generics import ListAPIView
from .serializer import WargaSerializer
from rest_framework.generics import RetrieveAPIView



class WargaListView(ListView):
    model = Warga
    paginate_by = 10

class WargaDetailView(DetailView):
    model = Warga

class WargaCreateView(CreateView):
    model = Warga
    fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga:warga-list')
    
class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('warga:pengaduan-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('warga:pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('warga:pengaduan-list')


class WargaUpdateView(UpdateView):
    model = Warga
    fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga:warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga:warga-list')

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
