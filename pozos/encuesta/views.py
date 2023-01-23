from django.http import HttpResponse
from django.views import generic
from encuesta.forms import ContestarForm
from encuesta.models import Encuesta
from encuesta.utils import RiesgoStat
from django.urls import reverse_lazy, reverse
from mapi.views import Pozo_APIView_Closest
from django.shortcuts import get_object_or_404, render
import json

def index(request):
     return HttpResponse("Hello, world. You're at the polls index.")

class ContestarEncuestaView(generic.CreateView):
    form_class = ContestarForm
    template_name = 'contestar.html'

    def get_success_url(self):
        return reverse_lazy('encuesta:resultado', kwargs={'pk': self.object.pk})

def getResultado(request, encuesta_id):
    encuesta = get_object_or_404(Encuesta, pk=encuesta_id)
    closest_pozo =  Pozo_APIView_Closest.as_view()(request=request,
                                          lat=encuesta.lat, 
                                          lon=encuesta.lon)
    rstats = RiesgoStat(encuesta, closest_pozo.data['pozo'])
    return render(request, 'resultado.html', {
        'encuesta' : encuesta,
        'pozo' : closest_pozo.data['pozo'],
        'stats' : rstats
    })

def error_404_view(request, exception):
    return render(request, '404.html')


