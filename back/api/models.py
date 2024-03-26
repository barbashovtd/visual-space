from django.db import models


class Appeal(models.Model):
    date_created = models.DateTimeField("Дата обращения", auto_now_add=True, editable=False)
    comment = models.TextField("Комментарий к обращению")
    date_updated = models.DateTimeField("Дата последнего обновления", auto_now=True, editable=False)
    phone = models.CharField("Телефон заказчика", max_length=15)  # я погуглил, максимальная длина номера 15 символов
    name = models.CharField("Имя заказчика", max_length=128, blank=False)
    notes = models.TextField("Заметки по заказу")

    def __str__(self):
        return f"{self.name} ({self.date_created})"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
