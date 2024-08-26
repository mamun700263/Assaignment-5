from django.urls import path
from .views import BookDetail
urlpatterns = [
    path('bookdetail/<int:pk>/', BookDetail.as_view(), name='detail'),
]
