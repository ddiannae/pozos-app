from django.urls import path

from encuesta import views

app_name = 'encuesta'
urlpatterns = [
    path('<int:pk>/', views.ResultadoEncuestaView.as_view(), name='resultado'),
    path('', views.ContestarEncuestaView.as_view(), name='contestar'),
]
