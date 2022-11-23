from rest_framework.response import Response
from rest_framework.views import APIView
from mapi.models import Pozo
from mapi.serializers import PozoSerializers

class Pozo_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        pozos = Pozo.objects.all()
        serializer = PozoSerializers(pozos, many=True)

        return Response(serializer.data)

class Pozo_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Pozo.objects.get(pk=pk)
        except Pozo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pozo = self.get_object(pk)
        serializer = PozoSerializers(pozo)
        return Response(serializer.data)
