from rest_framework import serializers
from mapi.models import Pozo

class PozoSerializers(serializers.ModelSerializer):
    alc_descripcion = serializers.ReadOnlyField()
    conduct_descripcion = serializers.ReadOnlyField()
    sdtm_sal_descripcion = serializers.ReadOnlyField()
    sdtm_ra_descripcion = serializers.ReadOnlyField()
    fluor_descripcion = serializers.ReadOnlyField()
    dur_descripcion = serializers.ReadOnlyField()
    coli_descripcion = serializers.ReadOnlyField()

    class Meta:
        model = Pozo 
        fields = '__all__'
