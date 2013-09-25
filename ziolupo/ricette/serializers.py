from django.conf import settings
from rest_framework import serializers, pagination


from .models import Portata,Categoria,Ricetta




__all__ = [
    'RicetteListSerializer',
    'RicetteDetailSerializer',
    'CategorieListSerializer',
    'CategorieDetailSerializer',
]


class CategorieListSerializer(serializers.ModelSerializer):
    """
    Categorie list
    """
    #details = serializers.HyperlinkedIdentityField(view_name='api_layer_detail', slug_field='slug')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Categoria

        #fields= (
        #   'nome', 'categoria',
        #    )

class CategorieDetailSerializer(serializers.ModelSerializer):
    """
    Categorie details
    """
    #details = serializers.HyperlinkedIdentityField(view_name='api_layer_detail', slug_field='slug')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Categoria

        #fields= (
        #   'nome', 'categoria',
        #    )
        
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



class RicetteDetailSerializer(serializers.ModelSerializer):
    """
    Ricette details
    """
    #details = serializers.HyperlinkedIdentityField(view_name='api_layer_detail', slug_field='slug')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Ricetta