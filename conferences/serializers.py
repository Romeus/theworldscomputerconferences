from rest_framework import serializers
from conferences.models import ConferenceType


class ConferenceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConferenceType
