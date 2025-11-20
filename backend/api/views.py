from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import (
    Portfolio, Contact, Team, Client, Student, Author, Book,
    )
from .serializers import (
    PortfolioSerializer, ContactSerializer, TeamSerializer, 
    ClientSerializer, StudentSerializer, AuthorSerializer,
    BookSerializer,
    )
from rest_framework import filters
from .pagination import StudentPagination

# new class-based view using ModelViewSet for Student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    search_fields = ['name']
    ordering_fields = ['name']
    filterset_fields = ['age']

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author")
    serializer_class = BookSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer