from django.contrib import admin
from django.urls import path
from rest_framework.schemas import get_schema_view

from visualspace.settings import DEBUG

urlpatterns = [
    path("admin/", admin.site.urls),
]

if DEBUG:
    urlpatterns.append(
        path(
            "openapi",
            get_schema_view(title="Visual Space", description="API", version="1.0.0"),
            name="openapi-schema",
        )
    )
