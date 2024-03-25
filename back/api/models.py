from django.db import models


class Appeal(models.Model):
    date_created = models.DateTimeField(verbose_name="дата обращения", auto_now_add=True, editable=False)
    comment = models.TextField(verbose_name="комментарий к обращению")
    date_updated = models.DateTimeField(verbose_name="дата последнего обновления", auto_now=True, editable=False)
    phone = models.CharField(
        verbose_name="телефон заказчика", max_length=15
    )  # я погуглил, максимальная длина номера 15 символов
    name = models.CharField(verbose_name="имя заказчика", max_length=128, blank=False)
    notes = models.TextField(verbose_name="заметки по заказу")

    def __str__(self):
        return f"{self.name} ({self.date_created})"

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "заявки"
