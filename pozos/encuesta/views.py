from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import AddForm
from django.urls import reverse_lazy


def index(request):
     return HttpResponse("Hello, world. You're at the polls index.")

class ContestarEncuestaView(CreateView):
    form_class = AddForm
    template_name = 'encuesta/contestar.html'
    success_url = reverse_lazy('encuesta:index')
