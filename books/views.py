from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookForm, ReviewForm
from .models import Book, Review
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator


def book_list(request):
    books = Book.objects.filter(sold=False)
    paginator = Paginator(books, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "books/book_list.html", {"page_obj": page_obj})


@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.seller = request.user
            book.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})


@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, "books/edit_book.html", {"form": form})


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "books/confirm_delete.html", {"book": book})


def search_results(request):
    query = request.GET.get("q", "")

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.none()

    return render(
        request, "books/search_results.html", {"books": books, "query": query}
    )


@login_required
def purchase_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # Process payment (this is a placeholder)
        return redirect("order_history")
    return render(request, "books/purchase_book.html", {"book": book})


@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect("book_detail", pk=pk)
    else:
        form = ReviewForm()
    return render(request, "books/add_review.html", {"form": form, "book": book})


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this review.")
    review.delete()
    return redirect("book_detail", pk=review.book.id)
