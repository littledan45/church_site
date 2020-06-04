from rest_framework.serializers import ModelSerializer

from churches.models import Church


class ChurchSerializer(ModelSerializer):
    class Meta:
        model = Church
        fields = ['id', 'name', 'street', 'city', 'province_state', 'country', 'mixlr_url']