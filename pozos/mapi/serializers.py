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
    alc_color = serializers.ReadOnlyField()
    conduct_color = serializers.ReadOnlyField()
    sdtm_sal_color = serializers.ReadOnlyField()
    sdtm_ra_color = serializers.ReadOnlyField()
    fluor_color = serializers.ReadOnlyField()
    dur_color = serializers.ReadOnlyField()
    coli_color = serializers.ReadOnlyField()

    class Meta:
        model = Pozo 
        fields = '__all__'
