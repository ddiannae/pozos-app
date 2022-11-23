from django.urls import path
from mapi.views import *

app_name = 'mapi'
urlpatterns = [
    path('pozo', Pozo_APIView.as_view(), name='pozos'), 
    path('pozo/<int:pk>/', Pozo_APIView_Detail.as_view()),
    
]
