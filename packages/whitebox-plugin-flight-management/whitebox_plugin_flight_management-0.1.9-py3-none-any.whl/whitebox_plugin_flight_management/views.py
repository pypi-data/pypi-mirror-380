import logging

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from .models import FlightSession
from .serializers import (
    FlightSessionSerializer,
)


logger = logging.getLogger(__name__)


class FlightSessionViewSet(GenericViewSet, ListModelMixin):
    queryset = FlightSession.objects.prefetch_related("recordings")
    serializer_class = FlightSessionSerializer
