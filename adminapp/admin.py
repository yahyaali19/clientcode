from django.contrib import admin

from .models import Representative, Deposit, Video


class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'target', 'daily_FTD', 'monthly_FTD')
    list_filter = ('name', 'target')
    search_fields = ['name']


class DepositAdmin(admin.ModelAdmin):
    list_display = ('representative', 'amount')
    list_filter = ('representative',)
    search_fields = ['representative']


# Register your models here.
admin.site.register(Representative, RepresentativeAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(Video)

