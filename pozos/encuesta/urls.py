from django.urls import path

from . import views

app_name = 'encuesta'
urlpatterns = [
    path('', views.index, name='index'),
    path('contestar/', views.ContestarEncuestaView.as_view(), name='contestar'),
]
