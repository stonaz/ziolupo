from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models import Q

from rest_framework import generics, permissions, authentication
from rest_framework.response import Response

from .models import Portata,Categoria,Ricetta
from .serializers import *

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
    #pagination_serializer_class = PaginatedLayerListSerializer
    #paginate_by_param = 'limit'
    #paginate_by = None

categorie_list = CategorieList.as_view()

class CategorieDetail(generics.RetrieveAPIView):
    """
    ### GET
    
    Retrieve categories'detail.
    
    """
    queryset = Categoria.objects.all()
    lookup_field = 'nome'
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= CategorieDetailSerializer
    #pagination_serializer_class = PaginatedLayerListSerializer
    #paginate_by_param = 'limit'
    #paginate_by = None

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
    #pagination_serializer_class = PaginatedLayerListSerializer
    #paginate_by_param = 'limit'
    #paginate_by = None
    
    def get_queryset(self):
        """
        Optionally restricts the returned recipes
        by filtering against a `search` query parameter in the URL.
        """
        # retrieve all nodes which are published and accessible to current user
        # and use joins to retrieve related fields
        queryset = Ricetta.objects.all()
        
        # retrieve value of querystring parameter "search"
        search = self.request.QUERY_PARAMS.get('search', None)
        
        if search is not None:
            search_query = (
                Q(nome__icontains=search) 
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
    #pagination_serializer_class = PaginatedLayerListSerializer
    #paginate_by_param = 'limit'
    #paginate_by = None

ricette_detail = RicetteDetail.as_view()


