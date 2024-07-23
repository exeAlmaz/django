from rest_framework import serializers

from measurement.models import Measurement, Sensor


# TODO: опишите необходимые сериализаторы
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'datetime']


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'datetime']


class SensorSerializer(serializers.ModelSerializer):
    sensors = MeasurementsSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'sensors']
