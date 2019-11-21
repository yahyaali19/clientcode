from . import models

from django.db.models import Sum


def calculate_progress_bar():
    target_total = models.Representative.objects.aggregate(Sum('target'))
    monthly_FTD_total = models.Representative.objects.aggregate(Sum('monthly_FTD'))
    return monthly_FTD_total/target_total * 100