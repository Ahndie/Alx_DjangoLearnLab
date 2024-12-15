from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# URL patterns for the API
urlpatterns = [
    path('', include(router.urls)),  # Includes all routes generated by the router
]
