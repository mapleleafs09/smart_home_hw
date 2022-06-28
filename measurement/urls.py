from django.urls import path

from measurement.views import ListCreateSensor, RetrieveUpdateSensor,  RetrieveAPIViewSensor, \
    ListAPIViewMeasurement

urlpatterns = [

    path('sensors/', ListCreateSensor.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensor.as_view()),
    path('measurement/', ListAPIViewMeasurement.as_view()),
    path('sensors/<pk>/', RetrieveAPIViewSensor.as_view()),
]
