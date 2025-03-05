from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import FormView,CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

# Create your views here.
class Login(LoginView):
    template_name = "user/login_form.html"
    fields = "__all__"
    redirect_authenticated_user = True

class Register(FormView):
    template_name = "user/register_form.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = "/login"
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('books')
        return super(Register,self).get(*args, **kwargs)
    
class BookLists(LoginRequiredMixin, ListView):
    """
    View to list all books for the authenticated user.
    """
    template_name = "user/library.html"
    model = Book
    context_object_name = "books"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.model.objects.filter(user=self.request.user)
        return context
    
class AddBook(LoginRequiredMixin, CreateView):

    model = Book
    template_name = "user/add_book.html"
    fields = ['title', 'file']
    success_url = reverse_lazy('books')
    template_name = "user/add_book.html"
    def form_valid(self, form):
        form.instance.user = self.request.user  # Привязываем задачу к текущему пользователю
        return super().form_valid(form)

class BookDelete(LoginRequiredMixin,DeleteView):
    model = Book
    context_object_name = "book"
    success_url = reverse_lazy("books")
    template_name = "user/delete_form.html"

class BookUpdate(LoginRequiredMixin,UpdateView):
    model = Book
    template_name = "user/update_book.html"
    fields = ['title','file']
    success_url = reverse_lazy('books')