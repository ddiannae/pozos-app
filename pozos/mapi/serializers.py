from rest_framework import serializers
from mapi.models import Pozo

class PozoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pozo 
        fields = '__all__'
