from django.conf import settings
from rest_framework import serializers, pagination


from .models import Categoria,Ricetta,Lista,CategoriaPreparazione,Preparazione




__all__ = [
    'RicetteListSerializer',
    'RicetteDetailSerializer',
    'CategorieListSerializer',
    'CategorieDetailSerializer',
    'PaginatedRicetteListSerializer',
    'ListeVelociListSerializer',
    'ListeVelociDetailSerializer',
    'CategoriePreparazioniListSerializer',
    'CategoriePreparazioniDetailSerializer',
    'PreparazioniDetailSerializer',
    'PreparazioniListSerializer'
]


class ListeVelociListSerializer(serializers.ModelSerializer):
    """
    Liste veloci list
    """
    details = serializers.HyperlinkedIdentityField(view_name='api_listeveloci_detail')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Lista
        
        
class CategoriePreparazioniListSerializer(serializers.ModelSerializer):
    """
    Categoria preparazione list
    """
    details = serializers.HyperlinkedIdentityField(view_name='api_categorie_preparazioni_detail')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = CategoriaPreparazione
        

        
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
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Ricetta

        fields= (
           'categoria','nome', 'difficulty','costo','time','image','details',
            )

        
class PreparazioniListSerializer(serializers.ModelSerializer):
    """
    Preparazioni list
    """
    details = serializers.HyperlinkedIdentityField(view_name='api_preparazioni_detail')
    categoria = serializers.Field(source='categoria.nome')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Preparazione

        fields= (
           'categoria','nome', 'details',
            )


class PaginatedRicetteListSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = RicetteListSerializer



class ListeVelociDetailSerializer(serializers.ModelSerializer):
    """
    Liste veloci details
    """
    #details = serializers.HyperlinkedIdentityField(view_name='api_layer_detail', slug_field='slug')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Lista


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
           'portata','nome', 'ricette'
            )


class PreparazioniDetailSerializer(serializers.ModelSerializer):
    """
    Preparazioni details
    """
    #details = serializers.HyperlinkedIdentityField(view_name='api_layer_detail', slug_field='slug')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = Preparazione
        
        
class CategoriePreparazioniDetailSerializer(serializers.ModelSerializer):
    """
    Categorie preparazioni details
    """
    #details = serializers.HyperlinkedIdentityField(view_name='api_layer_detail', slug_field='slug')
    #nodes = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_list', slug_field='slug')
    #geojson = serializers.HyperlinkedIdentityField(view_name='api_layer_nodes_geojson', slug_field='slug')
    
    class Meta:
        model = CategoriaPreparazione