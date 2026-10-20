from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=2)
    zip_code = models.CharField("CAP", max_length=5)
    country = models.CharField(max_length=100, default="Italia")
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    vat = models.CharField("Partita IVA", max_length=11, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.city}"
