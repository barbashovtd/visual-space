from django.http import HttpResponse
from django.contrib import admin
from .models import Appeal
from openpyxl import Workbook

import csv
import datetime


class AppealAdmin(admin.ModelAdmin):
    actions = ["export_as_xlsx", "export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta

        current_time_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename=Imported_csv_data_{current_time_str}.csv".format(meta)

        writer = csv.writer(response)

        field_names = ["name", "phone", "date_created", "date_updated", "comment", "notes", "id"]
        field_verbose_names = [
            "Имя заказчика",
            "Телефон заказчика",
            "Дата обращения",
            "Дата последнего обновления",
            "Комментарий к обращению",
            "Заметки по заказу",
            "ID в базе",
        ]

        writer.writerow(field_verbose_names)

        for obj in queryset:
            result = [getattr(obj, field) for field in field_names]

            result[2] = result[2].replace(tzinfo=None)
            result[3] = result[3].replace(tzinfo=None)

            writer.writerow(result)

        return response

    def export_as_xlsx(self, request, queryset):
        meta = self.model._meta

        current_time_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename=Imported_xslx_data_{current_time_str}.xlsx".format(
            meta
        )

        wb = Workbook()

        ws = wb.active
        ws.title = "Таблица Обращений"

        field_names = ["name", "phone", "date_created", "date_updated", "comment", "notes", "id"]

        field_verbose_names = [
            "Имя заказчика",
            "Телефон заказчика",
            "Дата обращения",
            "Дата последнего обновления",
            "Комментарий к обращению",
            "Заметки по заказу",
            "ID в базе",
        ]

        ws.append(field_verbose_names)

        for obj in queryset:
            result = [getattr(obj, field) for field in field_names]

            result[2] = result[2].replace(tzinfo=None)
            result[3] = result[3].replace(tzinfo=None)

            ws.append(result)

        wb.save(response)

        return response

    export_as_csv.short_description = "Экспортировать в csv выбранные поля"
    export_as_xlsx.short_description = "Экспортировать в xlsx выбранные поля"

    fieldsets = [
        (
            None,
            {
                "fields": [("name", "phone"), ("date_created", "date_updated"), "comment"],
            },
        ),
        ("Дополнительно", {"fields": ["notes"]}),
    ]
    readonly_fields = ("date_created", "date_updated")

    ordering = ("-date_created",)


admin.site.register(Appeal, AppealAdmin)
