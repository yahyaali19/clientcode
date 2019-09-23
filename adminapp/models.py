from django.db import models


# Create your models here.
class Representative(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    target = models.FloatField(blank=False)
    daily_FTD = models.FloatField(default=0)
    daily_amount = models.FloatField(default=0)
    monthly_FTD = models.FloatField(default=0)
    monthly_amount = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Deposit(models.Model):
    amount = models.FloatField()
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.representative.name, str(self.amount))


class Video(models.Model):
    video_key = models.CharField(max_length=1000)

    def __str__(self):
        return self.video_key
