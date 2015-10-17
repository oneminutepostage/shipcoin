from django.db import models

class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    amount  = models.DecimalField(max_digits=8, decimal_places=4)
    shippo_object_id = models.CharField(max_length=100, db_index=True)

class Label(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    rate  = models.ForeignKey(Rate, related_name= "label")
    amount  = models.DecimalField(max_digits=8, decimal_places=4)
    shippo_object_id = models.CharField(max_length=100, db_index=True)
    tracking_number = models.CharField(max_length=100, db_index=True)
    label_url = models.URLField(max_length=2048, blank=True)
