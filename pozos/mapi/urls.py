from django.urls import path, register_converter
from mapi.views import *
from . import converters 

app_name = 'mapi'

register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('pozo', Pozo_APIView.as_view(), name='pozos'), 
    path('pozo/<int:pk>/', Pozo_APIView_Detail.as_view()),
    path('cercano/<float:lat>/<float:lon>/', Pozo_APIView_Closest.as_view(), 
         name='closest'),
    
]
