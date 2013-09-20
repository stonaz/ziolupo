from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from rest_framework import generics, permissions, authentication
from rest_framework.response import Response

from .models import Portata,Categoria,Ricetta
from .serializers import *

class RicetteList(generics.ListCreateAPIView):
    """
    ### GET
    
    Retrieve list of recipes.
    
    ### POST
    
    Create new recipe if authorized (admins and allowed users only).
    """
    model= Ricetta
    queryset = Ricetta.objects.all()
    #permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    #authentication_classes = (authentication.SessionAuthentication,)
    serializer_class= RicetteListSerializer
    #pagination_serializer_class = PaginatedLayerListSerializer
    #paginate_by_param = 'limit'
    #paginate_by = None

ricette_list = RicetteList.as_view()
