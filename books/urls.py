from django.urls import path
from books import views

urlpatterns = [
    path('',views.books),
    path('index/', views.index, name= "index"),
    path('login/', views.books_login, name="login"),
    path("logout/", views.books_logout, name="logout"),

]

