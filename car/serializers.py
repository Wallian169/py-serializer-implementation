from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(min_value=0, max_value=1000)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
