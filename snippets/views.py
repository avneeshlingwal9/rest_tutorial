

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def snippet_list(request , format = None):

    # If request is GET, list all of them.
    # Else POST, add a new one. 

    if(request.method == 'GET'):

        queryset = Snippet.objects.all()

        serializer = SnippetSerializer(queryset, many= True)

        return Response(serializer.data)
    

    elif(request.method == 'POST'):

        serializer = SnippetSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):

            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    
    return Response({"error" : "Bad data"})

        


@api_view(['GET', 'PUT', 'DELETE'])

def snippet_detail(request, pk = None , format = None):


    try:
        snippet = Snippet.objects.get(pk = pk) 
    
    except Snippet.DoesNotExist:

        return Response(status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'GET':

        serializer = SnippetSerializer(snippet)

        return Response(serializer.data)
    
    elif request.method == 'PUT':


        serializer = SnippetSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.data, status.HTTP_404_NOT_FOUND)
    

    elif request.method == 'DELETE':

        snippet.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    


    return Response({'EROOR': "You messed up bro !"})