from django.db import models


class UserTypeChoice(models.TextChoices):
    BARBER = "BAR", "Barber"
    CUSTOMER = "CUS", "Customer"
