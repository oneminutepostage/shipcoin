from django.contrib import admin
import models

class RateAdmin(admin.ModelAdmin):
    model = models.Rate
    list_display = ["__unicode__", "amount", "created"]

class LabelAdmin(admin.ModelAdmin):
    model = models.Label
    list_display = ["__unicode__", "tracking_number", "amount", "created"]
    readonly_fields = ('rate',)

admin.site.register(models.Rate, RateAdmin)
admin.site.register(models.Label, LabelAdmin)
    