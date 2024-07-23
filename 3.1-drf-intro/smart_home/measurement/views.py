# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from .models import Measurement, Sensor
from .serializers import SensorSerializer, MeasurementSerializer, MeasurementsSerializer


# вывести весь список Сенсора
class SensorList(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Создать сенсор
class CreateSensor(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# удаление, обновление датчика
class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# создание измерений
class MeasurementCreate(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer



class SensorView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class Measurementlist(generics.ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer