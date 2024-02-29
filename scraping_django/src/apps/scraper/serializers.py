"""Serializers for two main models: ScrapedData and Keywords.
    Gives full data because the only allowed user is superuser."""

from rest_framework import serializers
from .models import Keywords, ScrapedData


class ScrapedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedData
        fields="__all__"


class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields="__all__"
