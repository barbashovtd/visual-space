from django.urls import path
from .views import CreateItem

urlpatterns = [path("appeal/", CreateItem.as_view(), name="appeal-create")]
