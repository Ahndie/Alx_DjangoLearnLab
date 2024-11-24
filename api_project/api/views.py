from rest_framework.generics import ListAPIView  # Import generics.ListAPIView
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Define the queryset for all Book objects
    serializer_class = BookSerializer  # Define the serializer for the data


