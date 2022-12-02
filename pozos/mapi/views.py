from rest_framework.response import Response
from rest_framework.views import APIView
from mapi.models import Pozo
from mapi.serializers import PozoSerializers
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from geopy.distance import distance as geopy_distance

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

class Pozo_APIView_Closest(APIView):
    def get(self, request, lat, lon, format=None):
        pnt = (lat, lon)
        pozos = Pozo.objects.all()
        sorted_pozos = sorted(pozos, 
                              key=lambda p: geopy_distance(p.ubicacion, pnt))
        closest_pozo = sorted_pozos[0]
        serializer = PozoSerializers(closest_pozo)
        distancia = geopy_distance(closest_pozo.ubicacion, pnt).km
        return Response({"pozo": serializer.data, 
                         "distancia": distancia})
