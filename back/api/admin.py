from django.contrib import admin
from .models import Appeal

# Register your models here.


class AppealAdminPage(admin.ModelAdmin):
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


admin.site.register(Appeal, AppealAdminPage)
