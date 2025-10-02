from rest_framework import serializers

from . import models


class MockProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MockProduct
        exclude = []


class MockStoreSerializer(serializers.ModelSerializer):
    products = MockProductSerializer(source="mockproduct_set", many=True)
    extra_code = serializers.CharField(default="test")

    class Meta:
        model = models.MockStore
        exclude = []
