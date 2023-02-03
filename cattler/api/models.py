from django.db import models


class Lot(models.Model):
    lot_number = models.PositiveIntegerField(primary_key=True)


class Troop(models.Model):
    troop_number = models.PositiveIntegerField()
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("troop_number", "lot"),)


class Animal(models.Model):
    caravan_number = models.PositiveIntegerField(unique=True, null=True, blank=True)
    RFID_number = models.PositiveIntegerField(null=True, blank=True)
    troop = models.ForeignKey(Troop, on_delete=models.CASCADE)


class Corral(models.Model):
    corral_number = models.AutoField(primary_key=True)
    troop = models.OneToOneField(Troop, on_delete=models.SET_NULL, null=True, blank=True)
