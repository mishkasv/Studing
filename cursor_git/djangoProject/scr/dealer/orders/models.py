from django.db import models


class Order(models.Model):
    PENDING = 'pending'
    AWAITING_PAYMENT = 'awaiting_payment'
    COMPLETED = 'completed'
    SHIPPED = 'shipped'
    CANCELLED = 'cancelled'
    DECLINED = 'declined'
    STATUS_OF_ORDER = (
        (PENDING, 'pending'),
        (COMPLETED, 'completed'),
        (AWAITING_PAYMENT, 'awaiting_payment'),
        (SHIPPED, 'shipped'),
        (CANCELLED, 'cancelled'),
        (DECLINED, 'declined'),
    )

    status = models.CharField(max_length=50, choices=STATUS_OF_ORDER, default=PENDING)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True, null=True)
    car = models.ForeignKey(
        'cars.Car',
        on_delete=models.CASCADE,
        related_name='order_car'
    )

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
