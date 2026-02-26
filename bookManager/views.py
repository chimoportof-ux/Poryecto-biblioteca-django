from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
from .forms import BookForm, CategoryForm
from django.contrib.auth.decorators import login_required
from .models import Book, Category


def home(request):
    return render(request, 'bookManager/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'bookManager/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('bookList')
            except IntegrityError:
                return render(request, 'bookManager/signup.html', {
                    'form': UserCreationForm(),
                    'error': 'This user is already taken'
                })
        else:
            return render(request, 'bookManager/signup.html', {
                'form': UserCreationForm(),
                'error': 'Password did not match'
            })

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'bookManager/login.html', {'form':AuthenticationForm()})
    else:
        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'bookManager/login.html', {'form':AuthenticationForm(), 'error': 'User name and password did not match'})
            else:
                login(request, user)
                return redirect('bookList')
        except Exception:
            return render(request, 'bookManager/login.html', {'form':AuthenticationForm(), 'error': 'Error'})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def bookList(request):
    books = Book.objects.all()
    category = Category.objects.all()
    return render(request, 'bookManager/bookList.html',{
        'books': books,
        'category': category,
    })

@login_required
def details(request, id):
    books = get_object_or_404(Book, id=id)
    category = Category.objects.all()
    return render(request, 'bookManager/details.html',{
        'books': books,
        'category': category,
    })

@login_required
def categoryList(request):
    category = Category.objects.all()
    return render(request, 'bookManager/categoryList.html',{
        'category': category,
    })

@login_required
def categoryBooks(request, id):
    category = get_object_or_404(Category, id=id)
    books = Book.objects.filter(category=category)
    return render(request, 'bookManager/categoryBook.html',{
        'books': books,
        'category': category,
    })

@login_required
def create_book(request):
    if request.method == 'GET':
        return render(request, 'bookManager/createBook.html', {
            'form': BookForm()
        })
    else:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            newbook = form.save(commit=False)
            newbook.user = request.user
            newbook.save()
            return redirect('bookList')
        else:
            return render(request, 'bookManager/createBook.html', {
                'form': form,
                'error': 'Bad data passed in. Try again.'
            })
        
@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('bookList')
    return render(request, 'bookManager/deleteBook.html', {
        'book': book
    })

@login_required
def modify_book(request, id):
    book=get_object_or_404(Book, id=id)
    if request.method == 'GET':
        form = BookForm(instance=book)
        return render(request, 'bookManager/modifyBook.html', {
            'book': book,
            'form': form,

        })
    else:
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect ('book-detail-page', book.id)
        else:
            return render(request, 'bookManager/modifyBook.html',{
                'book': book,
                'form': form,
                'error': 'Bad data passed in. Try again.'
            })

@login_required
def create_category(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'bookManager/createCategory.html', {
            'form': form,
        })
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            newcategory = form.save(commit=False)
            newcategory.user = request.user
            newcategory.save()
            return redirect('categoryList')
        else:
            return render(request, 'bookManager/createCategory.html', {
                'form': form,
                'error': 'Bad data passed in. Try again'
            })

# Create your views here.
