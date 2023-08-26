from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from books.models import Book, Customer , Loan 
from django.template import loader
from .forms import BookForm
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login , logout




def books(request):#display all books
    all_books = Book.objects.all()
    context = {
        'books': all_books
    }

    return render(request, 'books.html', context)


def add_book(request): #add a book to the list book
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')  # Redirect to the list of books
    else:
        form = BookForm()
    
    context = {'form': form}
    return render(request, 'add_book.html', context)


def search_books(request):
    query = request.GET.get('q')
    print("Query:", query)  # Print the query for debugging
    if query:
        books = Book.objects.filter(name__icontains=query)
        print("Books:", books)  # Print the books queryset for debugging
    else:
        books = []
    context = {
        'books': books,
        'query': query
    }
    return render(request, 'search_books.html', context)


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        book.delete()
        return HttpResponseRedirect('/books/')  # Redirect to the books list after deletion
    
    return render(request, 'delete_book.html', {'book': book})


def loan_book(request, book_id, customer_id):
    book = get_object_or_404(Book, pk=book_id)
    customer = get_object_or_404(Customer, pk=customer_id)


    # Calculate loan and return dates
    loandate = datetime.now().date()
    returndate = loandate + timedelta(days=14)  # Example: 2 weeks loan period

    # Create a new loan instance
    loan = Loan.objects.create(
        customer=customer,
        book=book,
        loandate=loandate,
        returndate=returndate,
    )

    # Update book availability
    book.available = False
    book.save()

    return render(request, 'loan_success.html', {'loan': loan})


def index(request):
    print("index function entered !!!!!!!!!!!!")
    return render(request, "index.html")


def books_login(request):
    print("login function entered !!!!!!!!!!!!")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"username={username}. password={password}")


        # Authenticate the user - validating user password. return user object if valid
        user = authenticate(request, username=username, password=password)
        print(f"authenticate passed. user is:{user}")


        if user is not None:
            # If the credentials are correct, log in the user
            login(request, user)
            print(f"** login passed. user is:{user}")
            return redirect('index')
        else:
            print(f"!! error login. user is:{user}")
            # If authentication fails, show an error message or redirect back to the login page
            error_message = "Invalid credentials. Please try again."
            return render(request, 'index.html', {'error_message': error_message})


    return redirect('index')


def books_logout(request):
    logout(request)
    
    return redirect('index')












