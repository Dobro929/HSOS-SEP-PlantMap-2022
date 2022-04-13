from bedApi.models import Bed, Geolocation
from django_grpc_framework import proto_serializers
from rest_framework import serializers


# https://stackoverflow.com/questions/53319787/how-can-i-select-specific-fields-in-django-rest-framework
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = '__all__'


class BedSerializer(DynamicFieldsModelSerializer):
    geolocation = GeolocationSerializer()

    class Meta:
        model = Bed
        fields = '__all__'
