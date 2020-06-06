from django.shortcuts import render
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Show, Theme
from .serializers import *

# Create your views here.

# Retrieve all shows.
@api_view(['GET'])
def shows_list(request):
    data = Show.objects.all()

    serializer = ShowSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)

# Retrieve all themes.
@api_view(['GET'])
def themes_list(request):
    data = Theme.objects.all()

    serializer = ThemeSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def show_finder(request, show):
    if len(show) > 1:
        data = Show.objects.filter(Q(name__icontains=show) | Q(english_name__icontains=show))
    else:
        data = []

    serializer = ShowSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def theme_finder(request, id):
    try:
        show = Show.objects.get(mal_id=id)
    except:
        show = None

    data = Theme.objects.filter(show=show)

    serializer = ThemeSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)

