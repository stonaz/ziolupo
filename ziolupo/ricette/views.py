from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models import Q
from django.conf import settings
from django.shortcuts import render

from rest_framework import generics, permissions, authentication
from rest_framework.response import Response

from .models import Categoria,Ricetta,Lista,CategoriaPreparazione,Preparazione
from .serializers import *

def index(request):
    return render(request,'ricette/index.html')


class CategoriePreparazioniList(generics.ListCreateAPIView):
    """
    ### GET
    
    Retrieve list of categories.
    
    ### POST
    
    Create new category if authorized (admins and allowed users only).
    """
    
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= CategoriePreparazioniListSerializer
    queryset = CategoriaPreparazione.objects.all()
    
categorie_preparazioni_list = CategoriePreparazioniList.as_view()


class CategoriePreparazioniDetail(generics.RetrieveAPIView):
    """
    ### GET
    
    
    
    """
    
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= CategoriePreparazioniDetailSerializer
    queryset = CategoriaPreparazione.objects.all()
    
categorie_preparazioni_detail = CategoriePreparazioniDetail.as_view()

class ListeVelociList(generics.ListCreateAPIView):
    """
    ### GET
    
    Retrieve list of categories.
    
    ### POST
    
    Create new category if authorized (admins and allowed users only).
    """
    
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= ListeVelociListSerializer
    queryset = Lista.objects.all()

listeveloci_list = ListeVelociList.as_view()


class ListeVelociDetail(generics.RetrieveAPIView):
    """
    ### GET
    
    Retrieve detail of lists.
    
    
    """
    
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= ListeVelociDetailSerializer
    queryset = Lista.objects.all()

listeveloci_detail = ListeVelociDetail.as_view()


class CategorieList(generics.ListCreateAPIView):
    """
    ### GET
    
    Retrieve list of categories.
    
    ### POST
    
    Create new category if authorized (admins and allowed users only).
    """
    
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= CategorieListSerializer
    queryset = Categoria.objects.all()

categorie_list = CategorieList.as_view()


class CategorieDetail(generics.RetrieveAPIView):
    """
    ### GET
    
    Retrieve categories'detail.
    
    """
    queryset = Categoria.objects.all()
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= CategorieDetailSerializer

categorie_detail = CategorieDetail.as_view()

class RicetteList(generics.ListCreateAPIView):
    """
    ### GET
    
    Retrieve list of recipes.
    
    ### POST
    
    Create new recipe if authorized (admins and allowed users only).
    """
    
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= RicetteListSerializer
    #pagination_serializer_class = PaginatedRicetteListSerializer
    #paginate_by_param = 'limit'
    #paginate_by = 2
    
    def get_queryset(self):
        """
        Optionally restricts the returned recipes
        by filtering against a `search` query parameter in the URL.
        """

        queryset = Ricetta.objects.all()
        
        # retrieve value of querystring parameter "search"
        search = self.request.QUERY_PARAMS.get('search', None)
        category= self.request.QUERY_PARAMS.get('category', None)
        lista= self.request.QUERY_PARAMS.get('lista', None)
        
        if search is not None:
            search_query = (
                Q(nome__icontains=search) 
            )
            # add instructions for search to queryset
            queryset = queryset.filter(search_query)
        
        if category is not None:
            search_query = (
                Q(categoria=category) 
            )
            # add instructions for search to queryset
            queryset = queryset.filter(search_query)
            
        if lista is not None:
            search_query = (
                Q(lista=lista) 
            )
            # add instructions for search to queryset
            queryset = queryset.filter(search_query)
        
        return queryset

ricette_list = RicetteList.as_view()

class RicetteDetail(generics.RetrieveAPIView):
    """
    ### GET
    
    Retrieve recipes'detail.
    
    """
    model= Ricetta
    queryset = Ricetta.objects.all()
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= RicetteDetailSerializer

ricette_detail = RicetteDetail.as_view()


class PreparazioniList(generics.ListCreateAPIView):
    """
    ### GET
    
    Retrieve list of recipes.
    
    ### POST
    
    Create new recipe if authorized (admins and allowed users only).
    """
    
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= PreparazioniListSerializer
    #pagination_serializer_class = PaginatedRicetteListSerializer
    #paginate_by_param = 'limit'
    #paginate_by = 2
    
    def get_queryset(self):
        """
        Optionally restricts the returned results
        by filtering against a `search` query parameter in the URL.
        """

        queryset = Preparazione.objects.all()
        
        # retrieve value of querystring parameter "search"
        category= self.request.QUERY_PARAMS.get('category', None)
        
        if category is not None:
            search_query = (
                Q(categoria=category) 
            )
            # add instructions for search to queryset
            queryset = queryset.filter(search_query)
        
        return queryset

preparazioni_list = PreparazioniList.as_view()


class PreparazioniDetail(generics.RetrieveAPIView):
    """
    ### GET
    
    Retrieve preparazioni'detail.
    
    """
    model= Preparazione
    queryset = Preparazione.objects.all()
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= PreparazioniDetailSerializer

preparazioni_detail = PreparazioniDetail.as_view()


