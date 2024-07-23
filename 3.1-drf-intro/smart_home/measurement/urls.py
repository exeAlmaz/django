from django.urls import path

from .views import SensorList, SensorDetail, CreateSensor, MeasurementCreate, SensorView, Measurementlist

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/all/', SensorList.as_view()),
    path('sensors/new/', CreateSensor.as_view()),
    path('sensors/<pk>/', SensorDetail.as_view()),
    path('sensors/del/', SensorDetail.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurement/all/', Measurementlist.as_view())

]
