from rest_framework import serializers

class city_serializer(serializers.Serializer):
    city=serializers.CharField(max_length=20,min_length=2,allow_null=False)

