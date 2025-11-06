from django.db import models

class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True)
    nama_lengkap = models.CharField(max_length=100)
    alamat = models.TextField()
    no_telepon = models.CharField(max_length=15, blank=True)
    tanggal_registrasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_lengkap


class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('BARU', 'Baru'),
        ('DIPROSES', 'Diproses'),
        ('SELESAI', 'Selesai'),
    ]

    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='BARU')
    tanggal_lapor = models.DateTimeField(auto_now_add=True)

    pelapor = models.ForeignKey(Warga, on_delete=models.CASCADE, related_name='pengaduan')

    def __str__(self):
        return self.judul
