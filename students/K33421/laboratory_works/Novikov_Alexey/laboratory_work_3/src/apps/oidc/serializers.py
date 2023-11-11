from rest_framework import serializers


class CustomJWTSerializerWithExpiration(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
    access_expiration = serializers.DateTimeField()
    refresh_expiration = serializers.DateTimeField()
