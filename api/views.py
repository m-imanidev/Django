from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


from books.serializers import BookSerializer, AuthorSerializer, PublisherSerializer
from books.views import Book, Author, Publisher

#-------------------------------- books --------------------------------
# list books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.filter(active=True)
    serializer_class = BookSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

# get information a book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
 

# create new book
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "book was created"}, status=200)
    return Response(serializer.errors, status=400)


#update infornation book
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"error": "book does not exist"}, status=404)
    serializer = BookSerializer(book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)



#-------------------------------- Authors --------------------------------

# list authors
@permission_classes([DjangoModelPermissionsOrAnonReadOnly])
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# create new author
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        author = serializer.save()
        return Response({"success": True, "data":{"id":author.id, "name": author.name}}, status=200)
    return Response(serializer.errors, status=400)

# get information a author
@permission_classes([AllowAny])
class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


#-------------------------------- Publisher --------------------------------
# list publishers
class PublisherListView(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

# create new publisher
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def publisher_create(request):
    serializer = PublisherSerializer(data=request.data)
    if serializer.is_valid():
        publisher = serializer.save()
        return Response({"success": True, "data":{"id":publisher.id, "name": publisher.name}}, status=200)
    return Response(serializer.errors, status=400)

# get information a publisher
@permission_classes([AllowAny])
class PublisherDetailView(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


#-------------------------------- Profile --------------------------------

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile_user(request):
    user = request.user
    try:
        token = Token.objects.get(user=user).key
    except Token.DoesNotExist:
        token = None
    data = {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "token": token
    }
    return Response(data)