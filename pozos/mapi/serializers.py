from rest_framework import serializers
from mapi.models import Pozo

class PozoSerializer(serializers.ModelSerializer):
    alc_descripcion = serializers.ReadOnlyField()
    conduct_descripcion = serializers.ReadOnlyField()
    sdtm_sal_descripcion = serializers.ReadOnlyField()
    sdtm_ra_descripcion = serializers.ReadOnlyField()
    fluor_descripcion = serializers.ReadOnlyField()
    dur_descripcion = serializers.ReadOnlyField()
    coli_descripcion = serializers.ReadOnlyField()
    nno3_descripcion = serializers.ReadOnlyField()
    as_descripcion = serializers.ReadOnlyField()
    cd_descripcion = serializers.ReadOnlyField()
    cr_descripcion = serializers.ReadOnlyField()
    hg_descripcion = serializers.ReadOnlyField()
    pb_descripcion = serializers.ReadOnlyField()
    mn_descripcion = serializers.ReadOnlyField()
    fe_descripcion = serializers.ReadOnlyField()
    alc_color = serializers.ReadOnlyField()
    conduct_color = serializers.ReadOnlyField()
    sdtm_sal_color = serializers.ReadOnlyField()
    sdtm_ra_color = serializers.ReadOnlyField()
    fluor_color = serializers.ReadOnlyField()
    dur_color = serializers.ReadOnlyField()
    coli_color = serializers.ReadOnlyField()
    nno3_color = serializers.ReadOnlyField()
    as_color = serializers.ReadOnlyField()
    cd_color = serializers.ReadOnlyField()
    cr_color = serializers.ReadOnlyField()
    hg_color = serializers.ReadOnlyField()
    pb_color = serializers.ReadOnlyField()
    mn_color = serializers.ReadOnlyField()
    fe_color = serializers.ReadOnlyField()

    class Meta:
        model = Pozo 
        exclude = ['id', 'periodo', 'clave']
