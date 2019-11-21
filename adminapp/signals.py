from . import models
from .utils import calculate_progress_bar, all_sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import random

@receiver(post_delete, sender=models.Deposit)
def deposit_deleted(sender, instance, *args, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "gossip", {
            "type": "user.gossip",
            "event": "Delete Deposit",
        }
    )

@receiver(post_save, sender=models.Deposit)
def deposit_added(sender, instance, created, **kwargs):
    if created:
        # Update FTD and amount
        representative = models.Representative.objects.get(name=instance.representative.name)
        representative.daily_FTD += 1
        representative.daily_amount += instance.amount
        representative.monthly_FTD += 1
        representative.monthly_amount += instance.amount
        representative._evil_extra_args = {'signal': False}
        representative.save()
        # Select a Random video and sent it as notification
        videos = models.Video.objects.all()
        count = videos.count()
        target_total, monthly_FTD_total, monthly_amount_total, daily_FTD_total, daily_amount_total = all_sum()
        if count > 0:
            random_video = random.randint(0, count - 1)
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "gossip", {
                    "type": "user.gossip",
                    "event": "New Deposit",
                    "username": representative.name,
                    "progress_bar": calculate_progress_bar(), 
                    "amount": instance.amount,
                    "video": videos[random_video].video_key,
                    "target_total": target_total,
                    "monthly_FTD_total": monthly_FTD_total,
                    "monthly_amount_total": monthly_amount_total,
                    "daily_FTD_total": daily_FTD_total,
                    "daily_amount_total": daily_amount_total
                }
            )

@receiver(post_save, sender=models.Representative)
def representative_added(sender, instance, created, **kwargs):
    if instance.name and not getattr(instance, '_evil_extra_args', False):
        representative = models.Representative.objects.get(name=instance.name)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gossip", {
                "type": "user.gossip",
                "event": "New Representative",
                "username": representative.name,
            }
        )

