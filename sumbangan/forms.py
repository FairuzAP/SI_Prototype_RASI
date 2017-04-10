from django import forms
from .models import PemberianSumbangan, PermintaanSumbangan

class PemberianForm(forms.ModelForm):
    class Meta:
        model = PemberianSumbangan
        fields = ('nama', 'no_ktp', 'email', 'no_telephone', 'jumlah', 'bukti_transfer')

class PermohonanForm(forms.ModelForm):
    class Meta:
        model = PermintaanSumbangan
        fields = ('nama', 'no_ktp', 'email', 'no_telephone', 'jumlah', 'alasan', 'attachment')