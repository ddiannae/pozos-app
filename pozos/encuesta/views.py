from django.http import HttpResponse
from django.views import generic
from encuesta.forms import ContestarForm
from encuesta.models import Encuesta
from django.urls import reverse_lazy, reverse
from mapi.views import Pozo_APIView_Closest

def index(request):
     return HttpResponse("Hello, world. You're at the polls index.")

class ContestarEncuestaView(generic.CreateView):
    form_class = ContestarForm
    template_name = 'contestar.html'

    def get_success_url(self):
        print(self.object)
        return reverse_lazy('encuesta:resultado', kwargs={'pk': self.object.pk})


#
class ResultadoEncuestaView(generic.DetailView):
    model = Encuesta 
    template_name = 'resultado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        closest_pozo =  Pozo_APIView_Closest.as_view()(request= self.request,
                                              lat=self.object.lat, 
                                              lon=self.object.lon)
        context['distancia'] = closest_pozo.data['distancia']
        context['pozo'] = closest_pozo.data["pozo"]
        return context

def error_404_view(request, exception):
    return render(request, '404.html')
