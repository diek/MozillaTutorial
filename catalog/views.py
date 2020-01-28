from catalog.models import Author, Book, BookInstance, Genre
from django.shortcuts import render
from django.views import generic
from locallibrary.settings import SITE_AUTHOR


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        "site_author": SITE_AUTHOR,
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    model = Book

    # def get_queryset(self):
    #     return Book.objects.[
    #         :5
    #     ]  # Get 5 books containing the title war


class BookDetailView(generic.DetailView):
    model = Book
