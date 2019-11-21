from . import models

from django.db.models import Sum


def calculate_progress_bar():
    target_total = models.Representative.objects.aggregate(Sum('target'))
    monthly_FTD_total = models.Representative.objects.aggregate(Sum('monthly_FTD'))
    return monthly_FTD_total['monthly_FTD__sum']/target_total['target__sum'] * 100

def all_sum():
    target_total = models.Representative.objects.aggregate(Sum('target'))
    monthly_FTD_total = models.Representative.objects.aggregate(Sum('monthly_FTD'))
    monthly_amount_total = models.Representative.objects.aggregate(Sum('monthly_amount'))
    daily_FTD_total = models.Representative.objects.aggregate(Sum('daily_FTD'))
    daily_amount_total = models.Representative.objects.aggregate(Sum('daily_amount'))
    return target_total, monthly_FTD_total, monthly_amount_total, daily_FTD_total, daily_amount_total