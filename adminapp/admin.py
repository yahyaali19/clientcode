import csv

from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path
from django.utils.http import urlquote

from .models import Representative, Deposit, Video


class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'target', 'daily_FTD', 'monthly_FTD')
    list_filter = ('name', 'target')
    search_fields = ['name']
    change_list_template = 'admin/representative.html'

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('/daily', self.admin_site.admin_view(self.ResetDaily), name='reset_daily'),
            path('/monthly', self.admin_site.admin_view(self.ResetMonthly), name='reset_monthly')
        ]
        return urls
    def ResetDaily(self, request):
        Representative.objects.all().update(daily_FTD=0, daily_amount=0)
        return redirect(request.META['HTTP_REFERER'])

    def ResetMonthly(self, request):
        Representative.objects.all().update(monthly_FTD=0, monthly_amount=0)
        return redirect(request.META['HTTP_REFERER'])

class DepositAdmin(admin.ModelAdmin):
    list_display = ('representative', 'amount', 'created_at')
    list_filter = ('representative', 'created_at')
    search_fields = ['representative__name']
    change_list_template = 'admin/deposit.html'

    def get_urls(self):
         urls = super().get_urls()
         urls += [
             path('/delete_deposit', self.admin_site.admin_view(self.deleteAllDeposits), name='delete_deposit'),
             path('/export', self.admin_site.admin_view(self.DownloadData), name='export_data')
         ]
         return urls

    def deleteAllDeposits(self, request):
        Deposit.objects.all().delete()
        return redirect(request.META['HTTP_REFERER'])

    def DownloadData(self, request):
        opts = Deposit._meta
        response = HttpResponse(content_type='text/csv')
        # force download.
        file_name = 'deposit.txt'
        response['Content-Disposition'] = 'attachment; filename={}'.format(urlquote(file_name))
        # the csv writer
        writer = csv.writer(response)
        field_names = [field.name for field in opts.fields]
        # Write a first row with header information
        writer.writerow(field_names)
        # Write data rows
        for obj in Deposit.objects.all():
            writer.writerow([getattr(obj, field) for field in field_names])
        return HttpResponse(response, content_type='text/csv')

# Register your models here.
admin.site.register(Representative, RepresentativeAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(Video)

