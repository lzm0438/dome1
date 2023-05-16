from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Student, Teacher, Book
from .serializers import StudentModelSerializer, TeacherModelSerializer, BookModelSerializer
from rest_framework import generics, filters
from rest_framework.generics import *
from django.http import HttpRequest


# from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class BookListView(ListAPIView, CreateAPIView, UpdateAPIView, ):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author']  # 筛选字段
    search_fields = ['title', 'author']  # 模糊查询字段
    ordering_fields = ['title', 'author']  # 排序字段
    pagination_class = PageNumberPagination




def fun_other(request: HttpRequest):
    user_id = request.GET.get("id", '')

