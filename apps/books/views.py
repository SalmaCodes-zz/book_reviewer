from django.shortcuts import render, redirect
from .models import *

# Create your views here.


# 'books/', displays all books.
def index(request):
    if 'user_id' not in request.session.keys():
        return redirect('/')
    context = {
        'reviews': Review.objects.order_by('-created_at'),
        'books': Book.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'books/books.html', context)


# 'books/add', displays form to add a book.
def add(request):
    if 'user_id' not in request.session.keys():
        return redirect('/')
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books/book_add.html', context)


# 'books/create', POST method to create a book.
def create(request):
    if request.method == 'POST':
        # Is there a new author?
        if len(request.POST['author_name']) > 0:
            author = Author.objects.create(name=request.POST['author_name'])
        else:
            author = Author.objects.get(id=request.POST['author_id'])
        book = Book.objects.create(
            title = request.POST['title'],
            author = author
        )
        review = Review.objects.create(
            rating = request.POST['rating'],
            content = request.POST['content'],
            book = book,
            reviewer = User.objects.get(id=request.session['user_id'])
        )
        return redirect('/books/{}'.format(book.id))
    return redirect('/books')


# 'books/<id>', displays the book with given id.
def display(request, id):
    if 'user_id' not in request.session.keys():
        return redirect('/')
    context = {
        'book': Book.objects.get(id=id)
    }
    return render(request, 'books/book.html', context)


# 'books/add/review', POST method to add a review to a book.
def add_review(request):
    if request.method == 'POST':
        book = Book.objects.get(id = request.POST['book_id'])
        Review.objects.create(
            rating = request.POST['rating'],
            content = request.POST['content'],
            book = book,
            reviewer = User.objects.get(id = request.session['user_id'])
        )
        return redirect('/books/{}'.format(book.id))


# 'books/<id>/delete', deletes the review with the given id.
def delete(request, id):
    review = Review.objects.get(id=id)
    book_id = review.book.id
    review.delete()
    return redirect('/books/{}'.format(book_id))

