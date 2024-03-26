from rest_framework.generics import CreateAPIView
from .models import Appeal
from .serializers import AppealSerializer


class CreateItem(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
