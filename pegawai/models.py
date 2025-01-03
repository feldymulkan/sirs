from django.db import models

class Pegawai(models.Model):
    nama = models.CharField(max_length = 150)
    nik = models.CharField(max_length=50, unique=True)
    jabatan = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nama
    
    
