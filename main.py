from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car):
    serializer = CarSerializer(car)
    json_data = JSONRenderer().render(serializer.data)
    return json_data


def deserialize_car_object(car_json):
    stream = BytesIO(car_json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return Car(**serializer.validated_data)
    else:
        raise ValueError(f"Invalid data: {serializer.errors}")
