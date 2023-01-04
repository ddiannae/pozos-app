from django.urls import path

from encuesta import views

app_name = 'encuesta'
urlpatterns = [
    path('<int:encuesta_id>/', views.getResultado, name='resultado'),
    path('', views.ContestarEncuestaView.as_view(), name='contestar'),
]
