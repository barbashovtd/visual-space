from django.contrib import admin
from .models import Appeal

# Register your models here.


class AppealAdminPage(admin.ModelAdmin):
    fieldsets = [
        (
            "Заявка",
            {
                "fields": ["name", "phone"],
            },
        ),
        (None, {"fields": ["date_created", "date_updated"]}),
        (None, {"fields": ["comment"]}),
        ("Дополнительно", {"fields": ["notes"]}),
    ]
    readonly_fields = ("date_created", "date_updated")


admin.site.register(Appeal, AppealAdminPage)
