from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("add_book/", views.add_book, name="add_book"),
    path("book/<int:pk>/", views.book_detail, name="book_detail"),
    path("book/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("book/<int:pk>/delete/", views.delete_book, name="delete_book"),
    path("search/", views.search_results, name="search_results"),
    path("book/<int:pk>/purchase/", views.purchase_book, name="purchase_book"),
    path("<int:pk>/review/", views.add_review, name="add_review"),
    path("review/<int:pk>/delete/", views.delete_review, name="delete_review"),
]
