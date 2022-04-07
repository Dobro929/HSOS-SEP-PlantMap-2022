from django_grpc_framework import proto_serializers
from bedApi.models import Bed

class BedSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = Bed
        fields = '__all__'