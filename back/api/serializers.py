from rest_framework import serializers
from .models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ["date_created", "comment", "date_updated", "phone", "name"]
