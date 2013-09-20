from django.conf import settings
from rest_framework import serializers, pagination


from .models import Portata,Categoria,Ricetta




__all__ = [
    'RicetteListSerializer',
]


class RicetteListSerializer(serializers.ModelSerializer):
    """
    Ricette list
    """
    #details = serializers.HyperlinkedIdentityField(view_name='api_layer_detail', slug_field='slug')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Ricetta

        #fields= (
        #   'nome', 'categoria',
        #    )

#class LayerDetailSerializer(LayerListSerializer):
#    """
#    Layer details
#    """
#    class Meta:
#        model = Layer
#        fields = ('name', 'center', 'area', 'zoom', 'is_external',
#                  'description', 'text', 'organization', 'website', 'nodes', 'geojson')

