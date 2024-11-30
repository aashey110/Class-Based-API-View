from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.BookListAPIView.as_view()),
    path('book_detail/<int:pk>/', views.BookDetialAPIView.as_view())
]
