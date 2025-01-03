# pegawai/forms.py

from django import forms
from .models import Pegawai

class PegawaiForm(forms.ModelForm):
    class Meta:
        model = Pegawai
        fields = ['nama', 'nik', 'jabatan']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Pegawai'}),
            'nik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nomor Induk Kepegawaian'}),
            'jabatan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jabatan'}),
        }
