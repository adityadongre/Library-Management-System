from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    outstanding_debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
