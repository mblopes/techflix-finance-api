from django.db import models

PAYMENT_WAY_CHOICES = {
    ('CREDIT CARD', 'Credit Card'),
    ('Debit', 'Debit'),
    ('BILLET', 'Billet')
}

ACCOUT_STATUS = {
    ('ACTIVATED', 'Activated'),
    ('DEACTIVATED', 'Deactivated')
}

PLAN_TYPE = {
    ('BASIC', 'Basic'),
    ('MEDIUM', 'Medium'),
    ('ULTRA', 'Ultra')
}

PAYMENT_STATUS = {
    ('LATE', 'Late'),
    ('PAID OUT', 'Paid Out'),
    ('OPEN', 'Open')
}

class Finance(models.Model):
    user_id = models.IntegerField(null=False)
    payment_way = models.CharField(max_length=50, choices=PAYMENT_WAY_CHOICES, null=False, blank=False)
    signature_date = models.DateField()
    status = models.CharField(max_length=50, choices=ACCOUT_STATUS, null=False, blank=False)
    plan_type = models.CharField(max_length=50, choices=PLAN_TYPE, null=False, blank=False)
    signature_value = models.DecimalField(max_digits=5, decimal_places=2)


class Payment(models.Model):
    user = models.ForeignKey(Finance, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS, null=False, blank=False)
    payment_value = models.DecimalField(max_digits=5, decimal_places=2)
