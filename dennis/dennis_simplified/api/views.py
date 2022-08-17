
from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Item
from .serializers import ItemSerialiser



@api_view(['GET'])          # we can give post, put, delete
def getData(request):
    # person = {'name': 'raju', 'age':28}
    items = Item.objects.all()
    serializer = ItemSerialiser(items, many = True)
    # return Response(person)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerialiser(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
