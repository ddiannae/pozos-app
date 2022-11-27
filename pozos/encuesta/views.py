from django.http import HttpResponse
from django.views import generic
from encuesta.forms import AddForm
from encuesta.models import Encuesta
from django.urls import reverse_lazy, reverse
from mapi.views import Pozo_APIView_Closest
import requests
import json

def index(request):
     return HttpResponse("Hello, world. You're at the polls index.")

class ContestarEncuestaView(generic.CreateView):
    form_class = AddForm
    template_name = 'contestar.html'

    def get_success_url(self):
        return reverse_lazy('encuesta:resultado', kwargs={'pk': self.object.pk})
#
class ResultadoEncuestaView(generic.DetailView):
    model = Encuesta 
    template_name = 'resultado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = 42
        response = Pozo_APIView_Closest.as_view()(request= self.request,
                                              lat=self.object.lat, 
                                              lon=self.object.lon)
        return context


