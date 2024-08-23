from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(min_value=0)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True,
        required=False
    )

    def validate(self, data):
        if not data.get("is_broken") and data.get("problem_description"):
            raise serializers.ValidationError(
                "Cannot provide a problem description "
                "if the car is not broken."
            )
        return data
