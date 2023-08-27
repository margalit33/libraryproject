
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
   path('index/', views.index, name= "index"),
   path('login/', views.books_login, name="login"),
   path("logout/", views.books_logout, name="books_logout"),
   path("booklist/", views.booklist, name="booklist"),
   path('all_loans/', views.all_loans, name='all_loans'),
   path('late_loans/', views.late_loans, name='late_loans'),
   path('return_book/<int:loan_id>/', views.return_book, name='return_book'),
]
















