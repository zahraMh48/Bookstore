from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin   #the login is neccessary /  mixin for class not def
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from .models import Book

class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'

# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name= 'books/book_detail.html'


@login_required
def book_detail_view(request, pk):
    #get book object
    book = get_object_or_404(Book, pk=pk)
    # get book comments
    book_comments = book.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid(): #if isnt valid the error will be send as form and we can see it
            new_comment = comment_form.save(commit=False) #form ro migire vali nemitize ti database
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()


    return render(request, 'books/book_detail.html', {'book':book,
                                                      'comments':book_comments,
                                                      'comment_form':comment_form,
                                                      })


class BookCreateView(LoginRequiredMixin, generic.CreateView):   # mixin is look like _base.html its a peace of pozzel and we use it in difrent part
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_create.html'


class BookUpdateView(LoginRequiredMixin,UserPassesTestMixin, generic.UpdateView): #userpassestestmixin habe an abstract user that we must rewrite it
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_update.html'

    def test_func(self):
        obj = self.get_object() #kodom ketab
        return obj.user == self.request.user


class BookDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
    def test_func(self):
        obj = self.get_object() #kodom ketab
        return obj.user == self.request.user








