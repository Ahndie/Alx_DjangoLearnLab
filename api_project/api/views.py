
from rest_framework.generics import ListAPIView  # Import generics.ListAPIView
from rest_framework import viewsets
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    (list, create, retrieve, update, destroy) for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookList(ListAPIView):
    queryset = Book.objects.all()  # Define the queryset for all Book objects
    serializer_class = BookSerializer  # Define the serializer for the data