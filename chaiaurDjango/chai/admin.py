from django.contrib import admin
from .models import Chaivariety,ChaiCertificate,ChairReview,Store
# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = ChairReview
    extra=2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','date_added','types')
    inlines=(ChaiReviewInline,)

class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_varities',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('name','certificate_number')

admin.site.register(Chaivariety,ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)