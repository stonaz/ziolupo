from django.conf import settings
from rest_framework import serializers, pagination


from .models import Portata,Categoria,Ricetta




__all__ = [
    'RicetteListSerializer',
    'RicetteDetailSerializer',
    'CategorieListSerializer',
    'CategorieDetailSerializer',
    'PortateListSerializer',
    'PortateDetailSerializer',
    'PortateCategorieSerializer',
    'PaginatedRicetteListSerializer',
]

class PortateListSerializer(serializers.ModelSerializer):
    """
    Portate list
    """
    details = serializers.HyperlinkedIdentityField(view_name='api_portate_detail', slug_field='nome')
    categorie = serializers.RelatedField(many=True)
    
    class Meta:
        model = Portata

        fields= (
           'nome', 'details','categorie',
            )

class PortateDetailSerializer(serializers.ModelSerializer):
    """
    Portate details
    """
    categorie = serializers.RelatedField(many=True)
    
    class Meta:
        model = Portata

        fields= (
           'nome','categorie'
            )
       
class PortateCategorieSerializer(serializers.ModelSerializer):
    """
    Portate/Categorie list
    """
    #details = serializers.HyperlinkedIdentityField(view_name='api_layer_detail', slug_field='slug')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Portata

        #fields= (
        #   'nome', 'categoria',
        #    )
        
class CategorieListSerializer(serializers.ModelSerializer):
    """
    Categorie list
    """
    details = serializers.HyperlinkedIdentityField(view_name='api_categorie_detail')
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
    details = serializers.HyperlinkedIdentityField(view_name='api_ricette_detail')
    categoria = serializers.Field(source='categoria.nome')
    portata =  serializers.Field(source='categoria.portata')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Ricetta

        fields= (
           'portata','categoria','nome', 'difficulty','costo','details',
            )

class PaginatedRicetteListSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = RicetteListSerializer

class RicetteDetailSerializer(serializers.ModelSerializer):
    """
    Ricette details
    """
    #details = serializers.HyperlinkedIdentityField(view_name='api_layer_detail', slug_field='slug')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Ricetta
        

class CategorieDetailSerializer(serializers.ModelSerializer):
    """
    Categorie details
    """
    ricette = RicetteListSerializer()
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Categoria

        fields= (
           'nome', 'ricette'
            )