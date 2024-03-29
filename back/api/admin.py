from django.http import HttpResponse
from django.contrib import admin
from .models import Appeal
from openpyxl import Workbook

import csv
import datetime


class AppealAdmin(admin.ModelAdmin):
    def __export_as(self, file_type, queryset):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

        content_type = {"csv": "text/csv", "xlsx": "application/vnd.ms-excel"}

        response = HttpResponse(content_type=content_type[file_type])
        response["Content-Disposition"] = f"attachment; filename=Imported_data_{current_time}.{file_type}"

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

        if file_type == "csv":
            writer = csv.writer(response)

            writer.writerow(field_verbose_names)

            for obj in queryset:
                result = [getattr(obj, field) for field in field_names]

                result[2] = result[2].replace(tzinfo=None)
                result[3] = result[3].replace(tzinfo=None)

                writer.writerow(result)
        else:
            wb = Workbook()

            ws = wb.active
            ws.title = "Таблица Обращений"

            ws.append(field_verbose_names)

            for obj in queryset:
                result = [getattr(obj, field) for field in field_names]

                result[2] = result[2].replace(tzinfo=None)
                result[3] = result[3].replace(tzinfo=None)

                ws.append(result)

            wb.save(response)

        return response

    actions = ["export_as_xlsx", "export_as_csv"]

    def export_as_csv(self, request, queryset):
        return self.__export_as("csv", queryset)

    def export_as_xlsx(self, request, queryset):
        return self.__export_as("xlsx", queryset)

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
