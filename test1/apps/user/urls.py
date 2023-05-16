from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from . import views

from django.urls import include
from rest_framework import routers

from . import views
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet, "students")

# 路由列表
urlpatterns = [
    path('docs/', include_docs_urls(title='user的页面标题')),
    path('books', views.BookListView.as_view(), name='book_list'),
    path("", include(router.urls))
]
