from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.


@csrf_exempt
def snippet_list(request):

    # If request is GET, list all of them.
    # Else POST, add a new one. 

    if(request.method == 'GET'):

        queryset = Snippet.objects.all()

        serializer = SnippetSerializer(queryset, many= True)

        return JsonResponse(serializer.data , safe = False)
    

    elif(request.method == 'POST'):

        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data = data)

        if serializer.is_valid():

            serializer.save()

            return JsonResponse(serializer.data, status_code = 200)
        
        return JsonResponse(serializer.data, status_code = 404)
    
    return JsonResponse({"error": "data corrupted"})

        


@csrf_exempt

def snippet_detail(request, pk = None):


    try:
        snippet = Snippet.objects.get(pk = pk) 
    
    except Snippet.DoesNotExist:

        return HttpResponse(status = 404)
    

    if request.method == 'GET':

        serializer = SnippetSerializer(snippet)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'PUT':

        data = JSONParser().parse(request)

        serializer = SnippetSerializer(data = data)

        if serializer.is_valid():

            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.data, status_code = 404)
    

    elif request.method == 'DELETE':

        snippet.delete()
        return HttpResponse(status = 204)
    


    return JsonResponse({'EROOR': "You messed up bro !"})