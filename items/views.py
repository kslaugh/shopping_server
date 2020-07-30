from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Items
from .serializers import *

@api_view(['GET', 'POST'])
def items_list(request):
    if request.method == 'GET':
        data = Items.objects.all()

        serializer = ItemSerializer(data, context={'request': request}, many=True)
        contdata={'data': serializer.data}

        return Response(contdata)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def items_detail(request, id):
    try:
        item = Items.objects.get(id=id)
    except Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        data = Items.objects.get(id=id)
        serializer = ItemSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)