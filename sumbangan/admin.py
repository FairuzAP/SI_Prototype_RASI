from django.contrib import admin
from .models import PemberianSumbangan, PermintaanSumbangan, TransaksiSumbangan

class PemberianAdmin(admin.ModelAdmin):
    date_hierarchy = 'tanggal'
    empty_value_display = '-empty-'
    exclude = ('is_validated',)

    list_display = ('tanggal', 'info_orang', 'jumlah', 'bukti_transfer', 'is_validated')
    list_display_links = ('info_orang',)
    list_filter = ('is_validated',)
    search_fields = ['nama', 'no_ktp']

    def info_orang(self, obj):
        return obj.no_ktp +", "+ obj.nama
    info_orang.short_description = 'Penyumbang'
    info_orang.admin_order_field = 'no_ktp'

    actions = ['validate_selected']

    def validate_selected(self, request, obj):
        for o in obj.all():
            t = TransaksiSumbangan()
            t.tanggal = o.tanggal
            t.pemberian = o
            t.permintaan = None
            t.jumlah = o.jumlah
            t.jenis = 'Pemberian'
            t.save()
            o.is_validated = True
            o.save()
    validate_selected.short_description = 'Validate selected transactions'
admin.site.register(PemberianSumbangan, PemberianAdmin)


class PermintaanAdmin(admin.ModelAdmin):
    date_hierarchy = 'tanggal'
    exclude = ('is_validated',)

    list_display = ('tanggal', 'info_orang', 'jumlah', 'alasan', 'is_validated')
    list_display_links = ('info_orang',)
    list_filter = ('is_validated',)
    search_fields = ['nama', 'no_ktp']

    def info_orang(self, obj):
        return obj.no_ktp +", "+ obj.nama
    info_orang.short_description = 'Penyumbang'
    info_orang.admin_order_field = 'no_ktp'

    actions = ['validate_selected']
    def validate_selected(self, request, obj):
        for o in obj.all():
            t = TransaksiSumbangan()
            t.tanggal = o.tanggal
            t.pemberian = None
            t.permintaan = o
            t.jumlah = -o.jumlah
            t.jenis = 'Permintaan'
            t.save()
            o.is_validated = True
            o.save()
    validate_selected.short_description = 'Validate selected transactions'
admin.site.register(PermintaanSumbangan, PermintaanAdmin)


class TransaksiAdmin(admin.ModelAdmin):
    date_hierarchy = 'tanggal'

    list_display = ('tanggal', 'info_orang', 'jumlah')
    list_display_links = None
    list_filter = ('jenis',)

    readonly_fields = ('tanggal', 'pemberian', 'permintaan', 'jumlah', 'jenis')

    def info_orang(self, obj):
        if obj.jenis == 'Pemberian':
            return obj.pemberian.no_ktp + ", " + obj.pemberian.nama
        else:
            return obj.permintaan.no_ktp + ", " + obj.permintaan.nama
    info_orang.short_description = 'Penyumbang/Pemohon'

    def has_add_permission(self, request):
        return False

    actions = ['delete_selected']
    def delete_selected(self, request, obj):
        for o in obj.all():
            if o.jenis == 'Pemberian':
                o.pemberian.is_validated = False;
                o.pemberian.save()
            else:
                o.permintaan.is_validated = False;
                o.permintaan.save()
            o.delete()
    delete_selected.short_description = 'Unvalidate selected transactions'
admin.site.register(TransaksiSumbangan, TransaksiAdmin)