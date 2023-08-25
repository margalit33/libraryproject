
from django.contrib import admin
from django.urls import path,include
from books import views

urlpatterns = [
   path('books/', views.books, name='books'), 
   path('admin/', admin.site.urls),
   path('add_book/',views.add_book, name='add_book'),
   path('search_books/', views.search_books, name='search_books'),
   path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
   path('loan/<int:book_id>/<int:customer_id>/', views.loan_book, name='loan_success'),
   path("login/", views.books_login, name="index"),
]









