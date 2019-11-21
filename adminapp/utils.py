from . import models

from django.db.models import Sum


def calculate_progress_bar():
    target_total = models.Representative.objects.aggregate(Sum('target'))
    monthly_FTD_total = models.Representative.objects.aggregate(Sum('monthly_FTD'))
    percentage = monthly_FTD_total['monthly_FTD__sum']/target_total['target__sum'] * 100
    return round(percentage, 2)

def all_sum():
    target_total = models.Representative.objects.aggregate(Sum('target'))['target__sum']
    monthly_FTD_total = models.Representative.objects.aggregate(Sum('monthly_FTD'))['monthly_FTD__sum']
    monthly_amount_total = models.Representative.objects.aggregate(Sum('monthly_amount'))['monthly_amount__sum']
    daily_FTD_total = models.Representative.objects.aggregate(Sum('daily_FTD'))['daily_FTD__sum']
    daily_amount_total = models.Representative.objects.aggregate(Sum('daily_amount'))['daily_amount__sum']
    return target_total, monthly_FTD_total, monthly_amount_total, daily_FTD_total, daily_amount_total
