
from rest_framework import permissions
from rest_framework import generics

from django.contrib.auth.models import User

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer , UserSerializer

from .permissions import IsOwnerOrReadOnly

# Create your views here.

class SnippetList(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()

    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        
        return serializer.save(owner = self.request.user)
    


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()

    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly ]


class UserList(generics.ListAPIView):

    queryset = User.objects.all()

    serializer_class = UserSerializer 


class UserDetail(generics.RetrieveAPIView):

    queryset = User.objects.all()

    serializer_class = UserSerializer

# Mixins. 
# class SnippetList(generics.GenericAPIView, mixins.ListModelMixin , mixins.CreateModelMixin):

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args,  **kwargs):

#         return self.list(request, args, kwargs)

#     def post(self, request, *args, **kwargs):

#         return self.list(request, args, kwargs) 
    

# class SnippetDetail(generics.GenericAPIView , mixins.UpdateModelMixin, mixins.DestroyModelMixin , mixins.RetrieveModelMixin):

#     queryset = Snippet.objects.all()

#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):

#         return self.retrieve(request, args, kwargs)
    
#     def put(self, request, *args, **kwargs):

#         return self.update(request, args, kwargs) 
    

#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)




# Class Based. 
# class SnippetList(APIView):


#     def get(self, request, format = None):

#         queryset = Snippet.objects.all()

#         serializer = SnippetSerializer(queryset, many = True)


#         return Response(serializer.data)

#     def post(self, request, format = None):
        
#         serializer = SnippetSerializer(data = request.data)

#         if serializer.is_valid(raise_exception = True):

#             serializer.save()

#             return Response(serializer, status = status.HTTP_201_CREATED)
        

#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

# class SnippetDetail(APIView):

#     def get_object(self, pk):

#         try: 
            
#             snippet = Snippet.objects.get(pk = pk)
        
#         except Snippet.DoesNotExist:

#             raise Http404


#     def get(self, request, pk , format = None):

#         snippet = self.get_object(pk)

#         print(snippet)

#         serializer = SnippetSerializer(snippet)

#         print(serializer.data)

#         return Response(serializer.data, status.HTTP_200_OK)


#     def put(self, request, pk , format = None):

#         snippet = self.get_object(pk)

#         serializer = SnippetSerializer(snippet, data = request.data)

#         if serializer.is_valid(raise_exception= True):

#             serializer.save()

#             return Response(serializer, status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



#     def delete(self, request, pk, format = None):
        
#         snippet = self.get_object(pk)

#         snippet.delete()

#         return Response(status = status.HTTP_204_NO_CONTENT)







## Function based; 

# @api_view(['GET', 'POST'])
# def snippet_list(request , format = None):

#     # If request is GET, list all of them.
#     # Else POST, add a new one. 

#     if(request.method == 'GET'):

#         queryset = Snippet.objects.all()

#         serializer = SnippetSerializer(queryset, many= True)

#         return Response(serializer.data)
    

#     elif(request.method == 'POST'):

#         serializer = SnippetSerializer(data = request.data)

#         if serializer.is_valid(raise_exception=True):

#             serializer.save()

#             return Response(serializer.data, status.HTTP_201_CREATED)
        
#         return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    
#     return Response({"error" : "Bad data"})

        


# @api_view(['GET', 'PUT', 'DELETE'])

# def snippet_detail(request, pk = None , format = None):


#     try:
#         snippet = Snippet.objects.get(pk = pk) 
    
#     except Snippet.DoesNotExist:

#         return Response(status.HTTP_400_BAD_REQUEST)
    

#     if request.method == 'GET':

#         serializer = SnippetSerializer(snippet)

#         return Response(serializer.data)
    
#     elif request.method == 'PUT':


#         serializer = SnippetSerializer(data = request.data)

#         if serializer.is_valid(raise_exception=True):

#             serializer.save()

#             return Response(serializer.data)

#         return Response(serializer.data, status.HTTP_404_NOT_FOUND)
    

#     elif request.method == 'DELETE':

#         snippet.delete()
#         return Response(status.HTTP_204_NO_CONTENT)
    


#     return Response({'EROOR': "You messed up bro !"})