from django.db import models
import os
import datetime


def bukti_transfer_directory_path(instance, filename):
    now = datetime.datetime.now().date()
    try:
        nextid = (PemberianSumbangan.objects.latest('id')).id + 1
    except(PemberianSumbangan.DoesNotExist):
        nextid = 0

    fname, file_extension = os.path.splitext(filename)
    return 'bukti_transfer/{0}/{1}/{2}_{3}{4}'.format(now.year, now.month, now.day, nextid, file_extension)
class PemberianSumbangan(models.Model):
    tanggal = models.DateField(auto_now_add=True, auto_now=False, db_index=True)
    nama = models.CharField(max_length=500)
    no_ktp = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, blank=True)
    no_telephone = models.CharField(max_length=50, blank=True)
    jumlah = models.DecimalField(max_digits=65, decimal_places=2)
    bukti_transfer = models.ImageField(upload_to=bukti_transfer_directory_path, max_length=500, blank=True)
    is_validated = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        if self.bukti_transfer:
            self.bukti_transfer.delete(save=True)
        super(PemberianSumbangan, self).delete(*args, **kwargs)

    def __str__(self):
        return self.tanggal.__str__() +" by: "+ self.no_ktp +", "+ self.nama +" : "+ self.jumlah.__str__()


def alasan_directory_path(instance, filename):
    now = datetime.datetime.now().date()
    try:
        nextid = (PermintaanSumbangan.objects.latest('id')).id + 1
    except(PermintaanSumbangan.DoesNotExist):
        nextid = 0

    fname, file_extension = os.path.splitext(filename)
    return 'alasan_permohonan/{0}/{1}/{2}_{3}{4}'.format(now.year, now.month, now.day, nextid, file_extension)
class PermintaanSumbangan(models.Model):
    tanggal = models.DateField(auto_now_add=True, auto_now=False, db_index=True)
    nama = models.CharField(max_length=500)
    no_ktp = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, blank=True)
    no_telephone = models.CharField(max_length=50, blank=True)
    jumlah = models.DecimalField(max_digits=65, decimal_places=2)
    alasan = models.TextField(max_length=2500, blank=True)
    attachment = models.FileField(upload_to=alasan_directory_path, max_length=500, blank=True)
    is_validated = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        if self.attachment:
            self.attachment.delete(save=True)
        super(PermintaanSumbangan, self).delete(*args, **kwargs)

    def __str__(self):
        return self.tanggal.__str__() +" by: "+ self.no_ktp +", "+ self.nama +" : "+ self.jumlah.__str__()


class TransaksiSumbangan(models.Model):
    tanggal = models.DateField(auto_now_add=False, auto_now=False, db_index=True)
    pemberian = models.ForeignKey(PemberianSumbangan, on_delete=models.CASCADE, blank=True, null=True)
    permintaan = models.ForeignKey(PermintaanSumbangan, on_delete=models.CASCADE, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=65, decimal_places=2)

    PEMBERIAN = 'Pemberian'
    PERMINTAAN = 'Permintaan'
    PILIHAN_TIPE_TRANSAKSI = (
        (PEMBERIAN, 'Pemberian'),
        (PERMINTAAN, 'Permintaan'),
    )
    jenis = models.CharField(max_length=50, choices=PILIHAN_TIPE_TRANSAKSI, default=PEMBERIAN)