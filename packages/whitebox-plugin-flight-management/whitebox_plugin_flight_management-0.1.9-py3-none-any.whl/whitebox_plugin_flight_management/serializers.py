from rest_framework import serializers

from .models import (
    FlightSession,
    FlightSessionRecording,
)


class EmbedFlightSessionRecordingSerializer(serializers.ModelSerializer):
    provided_by = serializers.CharField(source="get_provider")

    class Meta:
        model = FlightSessionRecording
        fields = [
            "id",
            "created_at",
            "file",
            "status",
            "provided_by",
            "provided_by_id",
        ]
        extra_kwargs = {
            "file": {
                "source": "get_file_url",
            },
        }


class FlightSessionSerializer(serializers.ModelSerializer):
    recordings = EmbedFlightSessionRecordingSerializer(many=True)

    class Meta:
        model = FlightSession
        fields = [
            "id",
            "name",
            "started_at",
            "ended_at",
            "recordings",
        ]
