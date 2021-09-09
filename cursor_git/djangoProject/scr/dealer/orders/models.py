from django.db import models, IntegrityError

models.Manager

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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """
        Save the current instance. Override this in a subclass if you want to
        control the saving process.

        The 'force_insert' and 'force_update' parameters can be used to insist
        that the "save" must be an SQL insert or update (or equivalent for
        non-SQL backends), respectively. Normally, they should not be set.
        """
        """
        CUSTOM
            If some order with same CAR and EMAIL or CAR and Phone exist, raise IntegrityError.
        """
        try:
            if Order.objects.get(email = self.email, car = self.car) or Order.objects.get(phone = self.phone, car = self.car):
                raise IntegrityError
        except models.ObjectDoesNotExist:
            self._prepare_related_fields_for_save(operation_name='save')

            using = using or router.db_for_write(self.__class__, instance=self)
            if force_insert and (force_update or update_fields):
                raise ValueError("Cannot force both insert and updating in model saving.")

            deferred_fields = self.get_deferred_fields()
            if update_fields is not None:
                # If update_fields is empty, skip the save. We do also check for
                # no-op saves later on for inheritance cases. This bailout is
                # still needed for skipping signal sending.
                if not update_fields:
                    return

                update_fields = frozenset(update_fields)
                field_names = set()

                for field in self._meta.concrete_fields:
                    if not field.primary_key:
                        field_names.add(field.name)

                        if field.name != field.attname:
                            field_names.add(field.attname)

                non_model_fields = update_fields.difference(field_names)

                if non_model_fields:
                    raise ValueError(
                        'The following fields do not exist in this model, are m2m '
                        'fields, or are non-concrete fields: %s'
                        % ', '.join(non_model_fields)
                    )

            # If saving to the same database, and this model is deferred, then
            # automatically do an "update_fields" save on the loaded fields.
            elif not force_insert and deferred_fields and using == self._state.db:
                field_names = set()
                for field in self._meta.concrete_fields:
                    if not field.primary_key and not hasattr(field, 'through'):
                        field_names.add(field.attname)
                loaded_fields = field_names.difference(deferred_fields)
                if loaded_fields:
                    update_fields = frozenset(loaded_fields)

            self.save_base(using=using, force_insert=force_insert,
                           force_update=force_update, update_fields=update_fields)
